from django.urls import path
from . import views


from .views import CustomLoginView 
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login/', CustomLoginView.as_view() , name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'),name= 'logout'),
    path('register/',views.RegisterPage , name='register'),
    path('info/', views.Info , name='info' ),

    path('profile/<str:pk>/', views.UserProfile , name='profile'),
    path('', views.Home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create/',views.Create,name='create'),
    path('edit/<str:pk>/',views.Update,name='update'),
    path('delete/<str:pk>/',views.Delete,name='delete'),
    path('deletemessage/<str:pk>/',views.DeleteMessage,name='deletemesage'),

    path('topiccreate/',views.AddTopic,name='createtopic'),
    path('profileedit/',views.EditProfile,name='profileedit'),


    
]