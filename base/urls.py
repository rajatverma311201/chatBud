from django.http import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.homePage, name="home"),
    path('room/<str:pk>/', views.roomPage, name="room"),
    path('create-room/', views.createRoom, name="createRoom"),
    path('update-room/<str:pk>/', views.updateRoom, name="updateRoom"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="deleteRoom"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="deleteMessage"),
    path('user-profile/<str:pk>/', views.userProfile, name="userProfile")
]
