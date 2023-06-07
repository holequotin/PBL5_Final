from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.core.paginator import Paginator
from .models import Exam
from .forms import *
from django.core.files.storage import default_storage
from django.http import HttpResponse
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

def exam_part_form(request,pk):
    exam = Exam.objects.get(id = pk)
    form = AddExamPartForm(request.POST or None)
    if request.method == "POST":
        print("Hello")
        if form.is_valid():
            print("valid data")
            exam_part = form.save(commit=False)
            exam_part.exam = exam
            exam_part.save()
            return redirect('Exam:ExamPartDetail',pk = exam_part.id)
        else:
            print(form.errors)
            return HttpResponse("Error")
    
    return render(request,'partials/add_exam_part_form.html',{'form' : form,'exam' : exam})   

def exam_list(request,number):
    search = request.GET.get('search')
    if search == '' or search is None:
        search = ''
        exams = Exam.objects.all().filter(user=request.user)
    else:
        exams = Exam.objects.filter(name__icontains = search, user = request.user)
    filter_level = request.GET.get('select-level')
    print(filter_level)
    if filter_level != 'All':
        filter_level = get_object_or_404(Level,name = filter_level)
        exams = exams.filter(level = filter_level,user =request.user)
    paginator = Paginator(exams,10)
    page_obj = paginator.page(number)
    context = {
        'page_obj' : page_obj,
        'search' :search,
        'number' : number
    }
    return render(request,'partials/exam_list.html',context)

def skill_list(request,number):
    search = request.GET.get('search')
    if search == '' or search is None:
        search = ''
        exams = ExamPart.objects.filter(user=request.user)
    else:
        exams = ExamPart.objects.filter(name__icontains = search, user = request.user)
    filter_level = request.GET.get('select-level')
    if filter_level != 'All':
        exams = exams.filter(level = filter_level,user =request.user)
    paginator = Paginator(exams,10)
    page_obj = paginator.page(number)
    context = {
        'page_obj' : page_obj,
        'search' :search,
        'number' : number
    }
    return render(request,'partials/exam_list.html',context)

def group_question_form(request,pk):
    if request.method == "POST" :
        form = AddGroupQuesitonForm(request.POST or None,request.FILES)
        if form.is_valid():
            group_question = form.save(commit=False)
            part = get_object_or_404(ExamPart,id = pk)
            group_question.exam_part = part
            group_question.save()    
            print("Saved")                                                                                                                                                                                                                                            
            # return render(request,'partials/group_question_detail.html',{'group' : group_question})
            return redirect('Teacher:AddExamDetail',pk = part.exam.id)
    form = AddGroupQuesitonForm()
    return render(request,'partials/add_group_question_form.html', {'form' : form,'part_id' : pk})

def group_skill_form(request,pk):
    if request.method == "POST" :
        form = AddGroupQuesitonForm(request.POST or None,request.FILES)
        if form.is_valid():
            group_question = form.save(commit=False)
            part = get_object_or_404(ExamPart,id = pk)
            group_question.exam_part = part
            group_question.save()    
            print("Saved")                                                                                                                                                                                                                                            
            # return render(request,'partials/group_question_detail.html',{'group' : group_question})
            return redirect('Teacher:AddExamSkillDetail',pk = part.id)
    form = AddGroupQuesitonForm()
    return render(request,'partials/add_group_skill_form.html', {'form' : form,'part_id' : pk})

def exam_part_detail(request,pk):
    part = get_object_or_404(ExamPart,id = pk)
    context = {
        'part' : part
    }
    return render(request,'partials/exam_part_detail.html',context)

def question_detail(request,pk):
    question = get_object_or_404(Question,id = pk)
    return render(request,'partials/question_detail.html',{'question' : question })

def question_form(request,pk):
    if request.method == "POST":
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            group_question = get_object_or_404(GroupQuestion,id = pk)
            question.group_question = group_question
            question.save()
            return redirect('Teacher:AddExamDetail', pk = group_question.exam_part.exam.id)
        else:
            print("Is not valid")
    form = AddQuestionForm()
    return render(request,'partials/add_question_form.html',{'form' : form , "pk" : pk})

def question_skill_form(request,pk):
    if request.method == "POST":
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            group_question = get_object_or_404(GroupQuestion,id = pk)
            question.group_question = group_question
            question.save()
            return redirect('Teacher:AddExamSkillDetail', pk = group_question.exam_part.id)
        else:
            print("Is not valid")
    form = AddQuestionForm()
    return render(request,'partials/add_question_skill_form.html',{'form' : form , "pk" : pk})

def delete_part(request,pk):
    part = get_object_or_404(ExamPart,id = pk)
    part.delete()
    return HttpResponse('')

def delete_question(request,pk):
    question = get_object_or_404(Question,id = pk)
    question.delete()
    return HttpResponse('')

def delete_group_question(request,pk):
    group = get_object_or_404(GroupQuestion,id = pk)
    group.delete()
    return HttpResponse('')

def update_question_content(request,pk):
    name = "content-question-" + str(pk)
    content = request.POST.get(name)
    question = Question.objects.get(id = pk)
    question.content = content
    question.save()
    return redirect('Exam:QuestionDetail',pk = pk)
def update_question_form(request,pk):
    question = get_object_or_404(Question,id=pk)
    if request.method == "POST":
        form = AddQuestionForm(request.POST,instance=question)
        if form.is_valid():
            # question = form.save(commit=False)
            # group_question = get_object_or_404(GroupQuestion,id = pk)
            # question.group_question = group_question
            # question.save()
            form.save()
            print('question saved')
            return redirect('Teacher:AddExamDetail', pk = question.group_question.exam_part.exam.id)
        else:
            print("Is not valid")
    form = AddQuestionForm(instance=question)
    return render(request,'partials/update_question_form.html',{'form' : form , "pk" : pk})

def update_question_skill_form(request,pk):
    question = get_object_or_404(Question,id = pk)
    if request.method == "POST":
        form = AddQuestionForm(request.POST,instance=question)
        if form.is_valid():
            # question = form.save(commit=False)
            # group_question = get_object_or_404(GroupQuestion,id = pk)
            # question.group_question = group_question
            # question.save()
            form.save()
            print('question saved')
            return redirect('Teacher:AddExamSkillDetail', pk = question.group_question.exam_part.id)
        else:
            print("Is not valid")
    form = AddQuestionForm(instance=question)
    return render(request,'partials/update_question_skill_form.html',{'form' : form , "pk" : pk})

def update_answer(request,pk):
    name = "answer-question-" + str(pk)
    answer = request.POST.get(name)
    question = Question.objects.get(id = pk)
    question.correct = answer
    question.save()
    return redirect('Exam:QuestionDetail',pk = pk)

#pk : group question id
def update_group_question(request,pk):
    group_question = get_object_or_404(GroupQuestion,id = pk)
    if request.method == "POST" :
        form = AddGroupQuesitonForm(request.POST or None,request.FILES,instance=group_question)
        if form.is_valid():
            form.save()
            print("Saved")                                                                                                                                                                                                                                            
            # return render(request,'partials/group_question_detail.html',{'group' : group_question})
            return redirect('Teacher:AddExamDetail',pk = form.instance.exam_part.exam.id)
    form = AddGroupQuesitonForm(instance=group_question)
    return render(request,'partials/update_group_question_form.html', {'form' : form,'part_id' : group_question.exam_part.id})

def update_group_skill(request,pk):
    group_question = get_object_or_404(GroupQuestion,id = pk)   
    if request.method == "POST" :
        form = AddGroupQuesitonForm(request.POST or None,request.FILES,instance=group_question)
        if form.is_valid():
            form.save()
            print("Saved")                                                                                                                                                                                                                                            
            # return render(request,'partials/group_question_detail.html',{'group' : group_question})
            return redirect('Teacher:AddExamSkillDetail',pk = form.instance.exam_part.id)
    form = AddGroupQuesitonForm(instance=group_question)  
    return render(request,'partials/update_group_skill_form.html', {'form' : form,'part_id' : group_question.exam_part.id})   

def delete_form(request):
    return HttpResponse('')