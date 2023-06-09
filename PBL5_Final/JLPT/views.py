from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from .models import Profile
from .test_funcs import *
from .groups import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
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
                request.session['filter_level'] = ''
                request.session['filter_skill'] = ''
                return redirect('Teacher:TeacherHome')
            if user.groups.filter(name = 'Student'):
                print('Is student')
                request.session['level'] = ''
                request.session['skill'] = ''
                return redirect('Student:StudentHome')
            if user.is_superuser:
            # if profile.role == 'teacher':
            #     return redirect('jlpt:TeacherHome')
            # if profile.role == 'student':
            #     return render(request,'student_home.html',{})
                return redirect('Administer:Teacher')
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

@login_required(login_url='jlpt:Login')
def logout_page(request):
    user = request.user
    logout(request)
    return redirect('jlpt:Login')

@login_required(login_url='jlpt:Login')
def student_home(request):
    # user = request.user
    # profile = get_object_or_404(Profile,user = user)
    return render(request,'pages/teacher_home.html',{})

@login_required(login_url='jlpt:Login')
def user_info(request):
    user = request.user
    if user.groups.filter(name = 'Teacher').exists():
        role = 'teacher'
    if user.groups.filter(name = 'Student').exists():
        role = 'student'
    
    profile = Profile.objects.get(user = user)
    initial_value = {
        'first_name' : profile.user.first_name,
        'last_name' : profile.user.last_name,
        'email' : profile.user.email,
        'phone_num' : profile.phone_number
    }
    form = UserInfoForm(initial=initial_value)
    context = {
        'role' : role,
        'profile' : profile,
        'form' : form
    }
    return render(request,'pages/user_info.html',context)

@login_required(login_url='jlpt:Login')
def update_profile(request):
    profile = Profile.objects.get(user = request.user)
    user = User.objects.get(id = profile.user.id)
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']
            user.email = cleaned_data['email']
            profile.phone_number = cleaned_data['phone_num']
            profile.save()
            user.save()
            messages.success(request,'Cập nhật thông tin thành công')
            return redirect('jlpt:UserInfo')
        else:
            context = {
            'profile' : profile,
            'form' : form
            }
            return render(request,'pages/user_info.html',context)
    return redirect('jlpt:UserInfo')

@login_required(login_url='jlpt:Login')
def change_password(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile' : profile
    }
    return render(request,'pages/user_change_password.html',context)

@login_required(login_url='jlpt:Login')
def update_password(request):
    user = User.objects.get(id = request.user.id)
    if request.method == "POST":
        password = request.POST.get("password")
        if not request.user.check_password(password):
            messages.error(request,"Mật khẩu cũ không chính xác")
            return redirect('jlpt:ChangePassword')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if not password1 == password2:
            messages.error(request,"Xác nhận mật khẩu không đúng")
            return redirect('jlpt:ChangePassword')
        try:
            validate_password(password1)
            user.set_password(password1)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request,"Cập nhật mật khẩu thành công")
        except:
            messages.error(request,"Mật khẩu không đúng theo yêu cầu")
    return redirect('jlpt:ChangePassword')