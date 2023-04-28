from django.shortcuts import render,get_object_or_404,get_list_or_404
from JLPT.models import *
from Exam.models import *
import Exam.forms as ExamForms
from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
def teacher_home(request):
    user = request.user
    profile = get_object_or_404(Profile,user = user)
    return render(request,'pages/teacher_home.html',{'user' : user, 'profile' : profile})

def exam_manager(request):
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    exams = Exam.objects.all().filter(user = user)
    context = {
        'user' : user,
        'profile' :profile,
        'exams' : exams
    }
    return render(request,'pages/teacher_exam_manager.html',context)

def teacher_add_exam(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    if request.method == "POST":
        form = ExamForms.AddExamForm(request.POST,request.FILES)
        if form.is_valid():
            exam =  form.save(commit=False)
            exam.user = request.user
            exam.save()
            return redirect('Teacher:ExamManager')
    form = ExamForms.AddExamForm()
    context = {
        'form' : form,
        'user' : user,
        'profile' : profile
    }
    return render(request,'pages/teacher_add_exam.html',context)

def teacher_delete_exam(request,pk):
    exam = Exam.objects.get(id = pk)
    exam.delete()
    return HttpResponse('')