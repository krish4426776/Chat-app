from django.urls import path
from . import views


urlpatterns = [
path('' , views.GetRoutes ),
path('rooms/' , views.GetRooms ),
path('topics/' , views.GetTopics ),
path('rooms/<str:pk>/' , views.GetRoom ),
path('topics/<str:pk>/' , views.GetTopic ),
path('users/' , views.GetUsers ),
 path('users/<int:pk>/username/', views.GetUser),
]