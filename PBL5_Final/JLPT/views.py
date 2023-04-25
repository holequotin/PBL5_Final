from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
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
    return render(request,'index.html',{})

def teacher_home(request):
    return render(request,'home.html',{})