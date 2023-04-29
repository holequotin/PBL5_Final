from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import Exam
from .forms import *
# Create your views here.

def detail_exam(request,pk):
    exam = get_object_or_404(Exam,id = pk)
    form = AddExamForm(instance=exam)
    return render(request,'partials/exam_detail.html',{'form':form})

def edit_exam(request,pk):
    if request.method == "POST":
        pass
    exam = get_object_or_404(Exam,id = pk)
    form = AddExamForm(instance=exam)
    return render(request,'partials/edit_exam_form.html',{'form' : form})