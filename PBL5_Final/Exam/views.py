from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import Exam
from .forms import *
from django.core.files.storage import default_storage
# Create your views here.

def detail_exam(request,pk):
    exam = get_object_or_404(Exam,id = pk)
    form = AddExamForm(instance=exam)
    return render(request,'partials/exam_detail.html',{'form':form})

def edit_exam(request,pk):
    exam = get_object_or_404(Exam,id = pk)
    if request.method == "POST":
        print("POST")
        form = AddExamForm(request.POST, request.FILES,instance = exam)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('Teacher:DetailExam',pk=form.instance.id)
        else:
            print("Form is not valid")
            print(form.cleaned_data)
    form = AddExamForm(instance=exam)
    return render(request,'partials/edit_exam_form.html',{'form' : form})