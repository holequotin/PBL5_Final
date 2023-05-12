from django.shortcuts import render,get_object_or_404,get_list_or_404
from JLPT.models import *
from Exam.models import *
import Exam.forms as ExamForms
from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
<<<<<<< HEAD
from tablib import Dataset
from .resources import LevelResource, ExamResource, ExamPartResource, GroupQuestionResource, QuestionResource
from django.contrib import messages


=======
from django.core.paginator import Paginator
>>>>>>> 5a8c3c943e83a8463f6c7ec6c525567e1801821b
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
def importExcel(request, pk):
    if request.method == 'POST':
        exam = get_object_or_404(Exam, id=pk)
        exam_id = exam.id
        dataset = Dataset()
        try:
            new_file = request.FILES['my_file']
            imported_data = dataset.load(new_file.read(), format='xlsx')
            for data in imported_data:
                level_resource = LevelResource()
                exam_resource = ExamResource()
                exam_part_resource = ExamPartResource()
                group_question_resource = GroupQuestionResource()
                question_resource = QuestionResource()

                # Importing data to ExamPart model
                exam_part_name = data[4]
                exam_part = ExamPart.objects.filter(name=exam_part_name, exam=exam).first()
                if not exam_part:
                    exam_part = ExamPart.objects.create(name=exam_part_name, time=data[5], pass_score=data[6], exam=exam)
                    exam_part.save()

                # Importing data to GroupQuestion model
                group_question_content = data[7]
                group_question = GroupQuestion.objects.filter(content=group_question_content, exam_part=exam_part).first()
                if not group_question:
                    group_question = GroupQuestion.objects.create(content=group_question_content, exam_part=exam_part)
                    group_question.save()

                # Importing data to Question model
                new_question = Question()
                new_question.content = data[8]
                new_question.optionA = data[9]
                new_question.optionB = data[10]
                new_question.optionC = data[11]
                new_question.optionD = data[12]
                new_question.score = data[13]
                new_question.correct = data[14]
                new_question.group_question = group_question
                new_question.save()
                
            messages.success(request, 'Imported successfully.')
        except Exception as e:
            messages.error(request, f'An error occurred while importing the file: {e}')
    return render(request,'pages/form.html')
