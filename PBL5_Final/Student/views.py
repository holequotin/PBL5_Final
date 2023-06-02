from django.shortcuts import render,redirect
from JLPT.models import *
from Exam.models import *
from django.shortcuts import get_list_or_404,get_object_or_404
from .models import *
from datetime import timedelta
from django.db.models import Sum
from django.db.models import F
# Create your views here.
fs = FileSystemStorage(location=settings.MEDIA_ROOT)
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
    print(exams)
    context = {
        'exams' : exams
    }
    return render(request,'pages/student_exam_list.html',context )

def exam_detail(request,pk):
    exam = get_object_or_404(PracticeHistory,id = pk)
    context = {
        'exam' : exam
    }
    return render(request,'pages/student_exam_detail.html',context)

def practice_history_detail(request,pk):
    practice_history = get_object_or_404(PracticeHistory,id = pk)
    context = {
        'practice_history' : practice_history
    }
    return render(request,'pages/student_practice_history_detail.html',context)
def test_part(request,pk):
    part_history = get_object_or_404(PracticePartHistory,id = pk)
    if part_history.status:
        return redirect('Student:PracticeHistoryDetail',pk = part_history.practice_history.id)
    context = {
        'part_history' : part_history
    }
    return render(request,'pages/student_test_part.html',context)

def start_test(request,pk):
    exam = get_object_or_404(Exam,id = pk)
    if PracticeHistory.objects.filter(exam = exam,status = False).exists():
        print("Bạn có một bài chưa hoàn thành của exam này")
        practice_history = get_object_or_404(PracticeHistory,exam = exam,status = False)
        return redirect('Student:PracticeHistoryDetail', pk=practice_history.id)
    else:    
        practice_history = PracticeHistory(
            student = request.user,
            name = exam.name,
            level = exam.level,
            user = exam.user,
            image = exam.image,
            pass_score = exam.pass_score,
            exam = exam,
            status = False
        )
        practice_history.save()
        
        for part in practice_history.exam.parts():
            part_history = PracticePartHistory(
                name = part.name,
                duration = timedelta(minutes=part.time),
                pass_score = part.pass_score,
                practice_history = practice_history,
                status = False,
                time_left = timedelta(minutes=part.time)
            )
            part_history.save()
            for group in part.groups():
              group_history = GroupQuestionHistory(
                  part = part_history,
                  content = group.content,
                  file = group.file
              )  
              group_history.save()
              for question in group.questions():
                  question_history = QuestionHistory(
                      group_question = group_history,
                      content = question.content,
                      optionA = question.optionA,
                      optionB = question.optionB,
                      optionC = question.optionC,
                      optionD = question.optionD,
                      score = question.score,
                      correct = question.correct,
                  )
                  question_history.save()
        return redirect('Student:PracticeHistoryDetail', pk=practice_history.id)
    
def update_answer(request,pk):
    name = "answer-question-" + str(pk)
    answer = request.POST.get(name)
    question_history = QuestionHistory.objects.get(id = pk)
    question_history.answer = answer
    question_history.save()
    return redirect('Student:QuestionHistory',pk = pk)

def question_history_detail(request,pk):
    question_history = get_object_or_404(QuestionHistory,id = pk)
    return render(request,'partials/student_question_history.html',{'question' : question_history })
    return render(request,'pages/student_exam_list.html',context)

def exam_select_list(request):

    return render(request,'pages/student_select_exam_new.html')

def exam_n(request,level):
    level_obj = level
    context = {
        'level' : level_obj
    }
    return render(request,'pages/student_exam_N.html',context)

def complete_practice_part(request,pk):
    practice_part = get_object_or_404(PracticePartHistory,id = pk)
    practice_part.status = True
    practice_part.save()
    
    practice = get_object_or_404(PracticeHistory,id = practice_part.practice_history.id)
    practice.status = True
    
    #check practice was done
    for part in practice.parts():
        if not part.status:
            practice.status = False
            break
    
    practice.save()
    
    return redirect('Student:PracticeHistoryDetail',pk = practice_part.practice_history.id)

def practice_result(request,pk):
    #TODO : kiểm tra bài thi đã hoàn thành hay chưa
    result = {}
    answers = 'ABCD'
    base_score = {}
    practice = get_object_or_404(PracticeHistory,id = pk)
    for part in practice.parts():
        value = QuestionHistory.objects.filter(group_question__in = part.groups(),answer__exact = F('correct')).aggregate(sum = Sum('score'))
        total = QuestionHistory.objects.filter(group_question__in = part.groups()).aggregate(sum = Sum('score'))
        value = 0 if value['sum'] is None else value['sum']
        total = 0 if total['sum'] is None else total['sum']
        result[part.name] = value
        base_score[part.name] = total
    
    profile = Profile.objects.get(user = request.user)    
    practice.scored = sum(result.values())
    practice.base_score = sum(base_score.values())
    practice.save()
    context = {
        'result' : result,
        'base_score' : base_score,
        'profile' : profile,
        'practice' : practice
    }
    return render(request,'pages/student_practice_result.html',context)

def history_list(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    history_list = PracticeHistory.objects.filter(student = user)
    context = {
        'history_list' : history_list,
        'profile' : profile
    }
    return render(request,'pages/student_history_list.html',context)