from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def homePage(request):

    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains = q) |
                                Q(description__icontains=q))
    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(request,'base/home.html', context)


def roomPage(request,pk):
    room = Room.objects.get(id = pk)
    return render(request,'base/room.html',{'room':room})


def createRoom(request):
    form = RoomForm()

    if(request.method=='POST'):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if(request.method=='POST'):
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.method=='POST':
        room.delete()
        return redirect('home')

    return render(request,'base/delete.html',{'obj':room})


def loginUser(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password is incorrect')
    
    context = {}
    return render(request, 'base/login_page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


    


    
