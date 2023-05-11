from django.shortcuts import render,get_object_or_404,get_list_or_404
from JLPT.models import *
from Exam.models import *
import Exam.forms as ExamForms
from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.
def teacher_home(request):
    user = request.user
    profile = get_object_or_404(Profile,user = user)
    return render(request,'pages/teacher_home.html',{'user' : user, 'profile' : profile})

def exam_manager(request,number):
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    exams = Exam.objects.all().filter(user = user)
    paginator = Paginator(exams,10)
    page_obj = paginator.page(number)
    context = {
        'number' : number,
        'user' : user,
        'profile' :profile,
        'page_obj' : page_obj
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
            return redirect('Teacher:ExamManager',number = 1)
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

def teacher_detail_exam(request,pk):
    user = request.user
    profile = get_object_or_404(Profile,user = user)
    exam = get_object_or_404(Exam,id = pk)
    form = ExamForms.AddExamForm(instance=exam)
    context = {
        'user' :user,
        'profile': profile,
        'form' : form
    }
    return render(request,'pages/teacher_exam_detail.html',context)

def teacher_add_exam_detail(request,pk):
    user = request.user
    profile = get_object_or_404(Profile,user = user)
    exam = get_object_or_404(Exam,id = pk)
    context = {
        'user' : user,
        'profile' : profile,
        'exam' : exam
    }
    return render(request,'pages/teacher_add_exam_detail.html',context)