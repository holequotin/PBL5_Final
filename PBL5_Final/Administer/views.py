from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from JLPT.models import *
from Exam.models import *
from Bookapp.models import*
from Document.models import *
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,redirect

# Create your views here.
def administer_teacher(request):
    users = User.objects.filter(groups__name='Teacher')
    
    # Lấy hồ sơ (profile) của từng người dùng
    profiles = []
    for user in users:
        profile = get_object_or_404(Profile, user=user)
        profiles.append(profile)
    return render(
        request, "pages/administer_teacher.html", {"users": users, "profiles": profiles}
    )
def administer_student(request):
    users = User.objects.filter(groups__name='Student')
    
    # Lấy hồ sơ (profile) của từng người dùng
    profiles = []
    for user in users:
        profile = get_object_or_404(Profile, user=user)
        profiles.append(profile)
    return render(
        request, "pages/administer_student.html", {"user": users, "profiles": profiles}
    )
def administer_exam(request,number):
    user = request.user
    profile = Profile.objects.all()
    exams = Exam.objects.all()
    paginator = Paginator(exams, 10)
    page_obj = paginator.page(number)
    context = {"number": 1, "user": user, "profile": profile, "page_obj": page_obj}
    return render(
        request, "pages/administer_exam.html", context
    )
def administer_practice_history(request):
    users = User.objects.filter(groups__name='Student')
    
    # Lấy hồ sơ (profile) của từng người dùng
    profiles = []
    for user in users:
        profile = get_object_or_404(Profile, user=user)
        profiles.append(profile)
    return render(
        request, "pages/administer_practice_history.html", {"user": user, "profile": profile}
    )
def administer_document(request, number):
    print('Hello',number)
    user = request.user
    profile = Profile.objects.all()
    documents = Post.objects.all()
    paginator = Paginator(documents, 10)
    page_obj = paginator.page(number)
    context = {"number": 1, "user": user, "profile": profile, "page_obj": page_obj}
    return render(
        request, "pages/administer_document.html", context
    )

def new_document_page(request,number):
    documents = Post.objects.all()
    paginator = Paginator(documents, 10)
    page_obj = paginator.page(number)
    context = {"number": number,"page_obj": page_obj}
    return render(
        request, "partials/document_table.html", context
    )

def new_exam_page(request,number):
    exams = Exam.objects.all()
    paginator = Paginator(exams,10)
    page_obj = paginator.page(number)
    context = {"number": number,"page_obj": page_obj}
    return render(
        request, "partials/exam_table.html", context
    )

def administer_book(request):
    user = request.user
    profile = Profile.objects.all()
    books = Book.objects.all()
    paginator = Paginator(books, 10)
    page_obj = paginator.page(1)
    context = {
        "number": 1,
        "user": user,
        "profile": profile,
        "page_obj": page_obj
    }
    return render(request, "pages/administer_book.html", context)

    
def search_teacher(request):
    print("Hello")
    name = request.GET.get("search")
    print(name)
    if name == "" or None:
        users = User.objects.filter(groups__name='Teacher')
        # Lấy hồ sơ (profile) của từng người dùng
        profiles = []
        for user in users:
            profile = get_object_or_404(Profile, user=user)
            profiles.append(profile)
    else:
        users = User.objects.filter(
            Q(first_name__contains=name) | Q(last_name__contains=name),
            groups__name='Teacher',                          
        )
        # Lấy hồ sơ (profile) của từng người dùng
        profiles = []
        for user in users:
            profile = get_object_or_404(Profile, user=user)
            profiles.append(profile)
    return render(request,'partials/teacher_table.html',{"users": users, "profile": profiles})

def edit_teacher(request,pk):
    user = User.objects.get(id = pk)
    profile = Profile.objects.get(user = user)
    return render(request,'partials/edit_teacher_form.html',{'profile' : profile})

def edit_student(request,pk):
    user = User.objects.get(id = pk)
    profile = Profile.objects.get(user = user)
    return render(request,'partials/edit_student_form.html',{'profile' : profile})

def update_teacher(request,pk):
    user = User.objects.get(id = pk)
    profile = Profile.objects.get(user = user)
    first_name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    profile.phone_number = phone
    
    user.save()
    profile.save()
    messages.success(request,"Cập nhật thông tin thành công")
    return redirect('Administer:Teacher')

def update_student(request,pk):
    user = User.objects.get(id = pk)
    profile = Profile.objects.get(user = user)
    first_name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    profile.phone_number = phone
    
    user.save()
    profile.save()
    messages.success(request,"Cập nhật thông tin thành công")
    return redirect('Administer:Student')

def delete_teacher(request,pk):
    user = User.objects.get(id = pk)
    user.delete()
    messages.success(request,'Xóa giáo viên thành công')
    return redirect('Administer:Teacher')

def delete_student(request,pk):
    user = User.objects.get(id = pk)
    user.delete()
    messages.success(request,'Xóa học sinh thành công')
    return redirect('Administer:Student')

def reset_password(request,pk):
    user = User.objects.get(id = pk)
    user.set_password('cntt@12345')
    messages.success(request,'Đặt lại mật khẩu thành công')
    if user.groups.filter(name = 'Teacher').exists():
        return redirect('Administer:EditTeacher',pk = user.id)
    else:
        return redirect('Administer:EditStudent',pk=user.id)

def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponse("")

def detail_user(request, pk):
    user = User.objects.get(id=pk)
    profile = get_object_or_404(Profile, user=user)

    context = {"user": user, "profile": profile}
    return render(request, "pages/administer_detail.html", context)