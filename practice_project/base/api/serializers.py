from rest_framework.serializers import ModelSerializer
from base.models import Room , Topic
from django.contrib.auth.models import User

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'email']
        
