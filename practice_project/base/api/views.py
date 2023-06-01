from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room , Topic
from .serializers import RoomSerializer , TopicSerializer , UserSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def GetRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/topic',
         'GET /api/user',

    ]

    return Response(routes)

@api_view(['GET'])
def GetRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics , many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def GetRoom(request,pk):
    room = Room.objects.get(id = pk)
    serializer = RoomSerializer(room , many=False)
    return Response(serializer.data)


@api_view(['GET'])
def GetTopic(request , pk):
    topic = Topic.objects.get(id = pk)
    serializer = TopicSerializer(topic , many=False)
    return Response(serializer.data)


@api_view(['GET'])
def GetUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response({'username': serializer.data['username']})



