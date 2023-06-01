from . models import Room , Topic 
from django.contrib.auth.models import User
from django.forms import ModelForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields= '__all__'
        exclude = ['host' , 'participants']


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , ]




        