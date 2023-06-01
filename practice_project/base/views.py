from django.shortcuts import render , redirect
from .models import Room , Topic , Message
from . forms import RoomForm , TopicForm ,UserEditForm
from django.db.models import Q 
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.contrib.auth.models import User

#for login and logout
from django.contrib.auth.views import LoginView 
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm  # for user creation 
from django.contrib.auth import login


# rooms = [
#     {'id':1 ,'name':'room 1'},
#     {'id':2 ,'name':'room 2'},
#     {'id':3 ,'name':'room 3'},
#     {'id':4 ,'name':'room 4'},

# ]
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def RegisterPage(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request , user)
            return redirect('home')
        
        
           
                 
    context = {'form': form}
    return render(request , 'base/register.html' , context)

def Info(request):
    return render(request , 'base/info.html')


def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None   else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(host__username__icontains=q)

           
        )
    room_count = rooms.count()
    # rooms = Room.objects.all()
    topics =Topic.objects.all()
    messages = Message.objects.filter(Q(room__name__icontains = q)) # for getting all message 
    context={'rooms':rooms , 'topics':topics , 'room_count':room_count , 'messages':messages}
    
    return render(request,'base/home.html',context)

def room(request,pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i 
    room = Room.objects.get(id=pk)
    message = room.message_set.all()  #gets every message related to the room 
    participants = room.participants.all()

    if request.method =='POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room' , pk = room.id)
        
   
    context = {'rooms':room , 'messages':message , 'participants':participants}
    return render(request , 'base/room.html' , context )

@login_required(login_url=  'login')
def Create(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)  # to not save immediately  room .gost also needs to be added
            room.host = request.user
            room.save()
        return redirect('home')

    context = {'form':form}
    return render (request,'base/roomform.html' , context)

@login_required(login_url=  'login')
def Update(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=Room.objects.get(id=pk))

    if request.user != room.host:
        return HttpResponse("YOU ARE NOT ALLOWED HERE")
    
    if request.method == "POST":
        form = RoomForm(request.POST,instance=Room.objects.get(id=pk) )
        if form.is_valid():
            form.save()
        return redirect ('home')
    context = {'form':form}
    return render (request,'base/roomform.html' , context)


@login_required(login_url=  'login')
def Delete(request , pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("YOU ARE NOT ALLOWED HERE")
   
    if request.method == "POST":
        room.delete()
        return redirect('home')
    

    context = {'obj': room}
    return render(request,'base/delete.html' , context)


@login_required(login_url=  'login')
def DeleteMessage(request , pk):
    
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("YOU ARE NOT ALLOWED HERE")
   
    if request.method == "POST":
        message.delete()
        return redirect ('home')
    

    context = {'obj': message}
    return render(request,'base/delete.html' , context)

def UserProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()  #  user --->  Room (room) _set all gives all rooms 
    #to render Topic
    messages = user.message_set.all()

    topics = Topic.objects.all()

    context = {'user':user , 'rooms' : rooms , 'topics':topics , 'messages': messages}
    return render(request, 'base/userprofile.html' ,context)


def AddTopic(request):
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context= {'form':form}
    return render(request , 'base/topicform.html'  , context )

@login_required(login_url=  'login')
def EditProfile(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect ( 'profile' , pk=user.id )

    context = {'form' : form}
    return render (request , 'base/profileedit.html' , context)



