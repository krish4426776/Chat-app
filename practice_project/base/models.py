from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
       return self.name


class Room(models.Model):
    topic = models.ForeignKey(Topic , on_delete=models.SET_NULL , null=True) #topic can have many rooms but 1 room can only contain 1 topic
    name = models.CharField(max_length=250)
    description = models.TextField(null=True , blank=True)
    updated =models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(User,on_delete=models.SET_NULL , null=True )
    participants = models.ManyToManyField(User,related_name='participants' , blank=True) 
    

    def __str__(self):
       return self.name
   
    
    class Meta:
        ordering = ['-updated' , '-created']

class Message(models.Model):
    user =models.ForeignKey(User , on_delete=models.CASCADE) #user can create many ,essage but message is created by 1 user 
    room = models.ForeignKey(Room , on_delete=models.CASCADE) #room can have many message but message can be inside 1 room
    body =models.TextField(null = True)
    updated =models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ['-updated' , '-created']
    
    








