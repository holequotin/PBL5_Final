from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from JLPT.models import *
from Exam.models import *
from Bookapp.models import*
from Document.models import *
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
def administer_exam(request):
    user = request.user
    profile = Profile.objects.all()
    return render(
        request, "pages/administer_exam.html", {"user": user, "profile": profile}
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
def administer_document(request):
    user = request.user
    profile = Profile.objects.all()
    documents = Post.objects.all()
    paginator = Paginator(documents, 10)
    page_obj = paginator.page(1)
    context = {"number": 1, "user": user, "profile": profile, "page_obj": page_obj}
    return render(
        request, "pages/administer_document.html", context
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


 
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponse("")

def detail_user(request, pk):
    user = User.objects.get(id=pk)
    profile = get_object_or_404(Profile, user=user)

    context = {"user": user, "profile": profile}
    return render(request, "pages/administer_detail.html", context)