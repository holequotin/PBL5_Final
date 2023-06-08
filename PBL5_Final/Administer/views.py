from django.shortcuts import get_object_or_404, render
from JLPT.models import *
from Exam.models import *
from Document.models import *
# Create your views here.
def administer_teacher(request):
    users = User.objects.filter(groups__name='Teacher')
    
    # Lấy hồ sơ (profile) của từng người dùng
    profiles = []
    for user in users:
        profile = get_object_or_404(Profile, user=user)
        profiles.append(profile)
    return render(
        request, "pages/administer_teacher.html", {"users": users, "profile": profiles}
    )
def administer_student(request):
    users = User.objects.filter(groups__name='Student')
    
    # Lấy hồ sơ (profile) của từng người dùng
    profiles = []
    for user in users:
        profile = get_object_or_404(Profile, user=user)
        profiles.append(profile)
    return render(
        request, "pages/administer_student.html", {"user": users, "profile": profiles}
    )
def administer_exam(request):
    user = request.user
    profile = Profile.objects.all()
    return render(
        request, "pages/administer_exam.html", {"user": user, "profile": profile}
    )
def administer_practice_history(request):
    user = request.user
    profile = Profile.objects.all()
    return render(
        request, "pages/administer_practice_history.html", {"user": user, "profile": profile}
    )
def administer_document(request):
    user = request.user
    profile = Profile.objects.all()
    return render(
        request, "pages/administer_document.html", {"user": user, "profile": profile}
    )
def administer_book(request):
    user = request.user
    profile = Profile.objects.all()
    return render(
        request, "pages/administer_book.html", {"user": user, "profile": profile}
    )
