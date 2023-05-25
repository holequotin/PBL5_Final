from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Profile
from .test_funcs import *
from .groups import *
# Create your views here.

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username,password = password)
        if user is not None:
            profile = Profile.objects.get(user = user)
            login(request,user)
            if user.groups.filter(name = 'Teacher'):
                return redirect('Teacher:TeacherHome')
            if user.groups.filter(name = 'Student'):
                print('Is student')
                return redirect('Student:StudentHome')
            # if profile.role == 'teacher':
            #     return redirect('jlpt:TeacherHome')
            # if profile.role == 'student':
            #     return render(request,'student_home.html',{})
    return render(request,'pages/login.html',{'title' : 'Đăng nhập'})

def register_page(request):
    if request.method == "POST":
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1==password2 and password1 !="":        
            username = request.POST.get("username")
            first_name = request.POST.get("firstname")
            last_name = request.POST.get("lastname")
            user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name = last_name)
            profile = Profile.objects.create(user=user)
            user.groups.add(student_group)
            return redirect('jlpt:Login')
    return render(request,'pages/register.html',{'title':'Đăng ký'})

@login_required(login_url='jlpt:Login')
@user_passes_test(user_is_teacher)
def teacher_home(request):
    user = request.user
    profile = get_object_or_404(Profile,user = user)
    return render(request,'pages/teacher_home.html',{'user' : user, 'profile' : profile})

def logout_page(request):
    user = request.user
    logout(request)
    return redirect('jlpt:Login')

def student_home(request):
    # user = request.user
    # profile = get_object_or_404(Profile,user = user)
    return render(request,'pages/teacher_home.html',{})