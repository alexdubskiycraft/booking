from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mainapp.models import *



def signup_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'mainapp/signup.html', {'form': form})    

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'mainapp/login.html', {'form': form})  

@login_required
def index(request):
    context = {
        "render_string": "Hello, world!"
    }
    return render(request, "mainapp/index.html", context)

@login_required
def room_list(request):
    rooms = Room.objects.all()
    context = {
        "room_list": rooms,
    }
    return render(request, "mainapp/room_list.html", context)  

def user_list(request):
    users = User.objects.all()
    context = {
        "user_list": users,
    }
    return render(request, "user_list.html", context)

def booking_list(request):
    book = Booking.objects.all()
    context = {
        "booking_list": book,
    }
    return render(request, "booking_list.html", context)