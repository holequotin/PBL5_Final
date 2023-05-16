from django.shortcuts import render
from JLPT.models import *
from Exam.models import *
from django.shortcuts import get_list_or_404,get_object_or_404
# Create your views here.
def index(request):
    user = request.user
    profile = get_object_or_404(Profile,user = user)
    context = {
        'profile' : profile
    }
    return render(request,'pages/student_home.html',context)

def exam_list(request,level):
    level_obj = get_object_or_404(Level,name = level)
    exams = Exam.objects.all().filter(level = level_obj)
    context = {
        'exams' : exams
    }
    return render(request,'pages/student_exam_list.html',context)

def exam_select_list(request):

    return render(request,'pages/student_select_exam_new.html')

def exam_n(request,level):
    level_obj = level
    context = {
        'level' : level_obj
    }
    return render(request,'pages/student_exam_N.html',context)