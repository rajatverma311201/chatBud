from django.http import HttpResponse
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homePage,name="home"),
    path('room/<str:pk>/', views.roomPage, name="room"),
    path('create-room/', views.createRoom, name="createRoom"),
    path('update-room/<str:pk>/', views.updateRoom, name="updateRoom"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="deleteRoom")
]
