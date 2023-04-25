from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request,username = username,password = password)
        if user is not None:
            profile = Profile.objects.get(user = user)
            if profile.role == 'teacher':
                return render(request,'home.html',{})
            if profile.role == 'student':
                return render(request,'student_home.html',{})
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
            return redirect('jlpt:Login')
    return render(request,'pages/register.html',{'title':'Đăng ký'})

def teacher_home(request):
    return render(request,'home.html',{})