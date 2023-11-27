from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth

from django.contrib import messages
from .models import Student
from teacher_app.models import Teacher, Course, Assignmet


@login_required(login_url='base')
def home(request):
    current_user = request.user
    student = get_object_or_404(Student, user = current_user)
    print(student)
    student_courses = Course.objects.filter(students=student)
    print(student_courses)
    context = {
        'courses': student_courses,
    }
    return render(request, 'student_app/home.html', context)

def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    assignments = Assignmet.objects.filter(course = course)
    print(course, assignments)
    context = {
        'course' : course,
        'assignments' : assignments,
    }

    return render(request, 'student_app/course_detail.html', context)

def profile_view(request):
    pass

def submission_view(request, pk):
    if request.method == 'POST':
        pass

    assignment = Assignmet.objects.get(id=pk)
    context = {
        'assignment': assignment,
    }

    return render(request, 'student_app/submission.html', context)

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        session = request.POST.get('session')
        dept = request.POST.get('dept')
        stu_id = request.POST.get('stu_id')


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

                user_model = User.objects.get(username=username)
                new_student = Student.objects.create(user=user_model, stu_id = stu_id, session=session, dept=dept)
                new_student.save()
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')


    return render(request, 'student_app/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'student_app/login.html')  


@login_required(login_url='base')
def logout_view(request):
    auth.logout(request)
    return redirect('')

