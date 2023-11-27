from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth

from django.contrib import messages
from .models import Teacher


@login_required(login_url='base')
def home(request):

    return render(request, 'teacher_app/home.html')  

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        designation = request.POST.get('designation')

        print(first_name, last_name, email, username, email, designation)

        if password == password2:
            if username and User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif email and User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name = first_name, last_name = last_name)
                user.save()
                print(user)

                user_model = User.objects.get(username=username)
                new_teacher = Teacher.objects.create(user=user_model, designation = designation)
                new_teacher.save()
                print(new_teacher)
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')


    return render(request, 'teacher_app/register.html', {'form': "form"})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'teacher_app/login.html')  


@login_required(login_url='base')
def logout_view(request):
    auth.logout(request)
    return redirect('')

