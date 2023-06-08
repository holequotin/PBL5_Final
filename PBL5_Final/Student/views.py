import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from JLPT.models import *
from Exam.models import *
from django.shortcuts import get_list_or_404,get_object_or_404
from .models import *
from datetime import timedelta
from django.db.models import Sum
from django.db.models import F
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import user_passes_test,login_required
import JLPT.test_funcs
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
        'exams' : exams,
        'profile' : Profile.objects.get(user = request.user)
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
        'practice_history' : practice_history,
        'profile' : Profile.objects.get(user = request.user)
    }
    return render(request,'pages/student_practice_history_detail.html',context)
def test_part(request,pk):
    time = get_object_or_404(PracticePartHistory,id = pk)
    input = int(time.time_left.total_seconds())
    idSP = pk
    giay = input % 60
    phut= input // 60
    type = request.GET.get('type')
    if type != "skill":
        type = "test"
    part_history = get_object_or_404(PracticePartHistory,id = pk)
    if part_history.status == True and part_history.practice_history is not None:
        return redirect('Student:PracticeHistoryDetail', pk = part_history.practice_history.id) 
    if part_history.status == True and part_history is None:
        return redirect('Student:SkillResult',pk = part_history.id)
    context = {
        
        'part_history' : part_history,
        'input' : input,
        'phut' : phut,
        'giay': giay,
        'idSP' : idSP,
        'profile' : Profile.objects.get(user = request.user),
        'type' : type
    }
    return render(request,'pages/student_test_part.html',context)

        # if part_his.status == True and part_his.practice_history is None:
        #     return redirect('Student:SkillResult',pk = part_his.id)
def start_skill_exam(request,pk):
    part = get_object_or_404(ExamPart,id = pk)
    time = part.time * 60
    input = time
    idSP = pk
    giay = input % 60
    phut= input // 60
    context = {
        'profile' : Profile.objects.get(user = request.user),
        'type' : 'skill',
        'input' : input,
        'phut' : phut,
        'giay': giay,
        'idSP' : idSP,  
    }
    #TODO: Chinh ali
    if PracticePartHistory.objects.filter(part = part,status = False,student = request.user).exists():
        # part_his = PracticePartHistory.objects.filter(part = part,status = False).first()
        # context['part_history'] = part_his
        parts = get_list_or_404(PracticePartHistory,part = part,status = False,student = request.user)
        messages.warning(request,f"Bạn có {len(parts)} bài thi chưa hoàn thành của exam này, có muốn tiếp tục làm bài ?")
        request.session['part_id'] = part.id
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    part_history = PracticePartHistory(
                student = request.user,
                name = part.name,
                duration = timedelta(minutes=part.time),
                pass_score = part.pass_score,
                part = part,
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
    context['part_history'] = part_history
    return render(request,'pages/student_test_part.html',context)    

def start_test(request,pk):
    exam = get_object_or_404(Exam,id = pk)
    if PracticeHistory.objects.filter(exam = exam,status = False,student = request.user).exists():
        practice_history = get_list_or_404(PracticeHistory,exam = exam,status = False,student = request.user)
        messages.warning(request,f"Bạn có {len(practice_history)} bài thi chưa hoàn thành của exam này, có muốn tiếp tục làm bài ?")
        #messages.info(request,str(practice_history.id))
        #request.session['practice_id'] = practice_history.id
        request.session['exam_id'] = exam.id
        return redirect(request.META.get('HTTP_REFERER', '/'))
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

def new_skill_exam(request,pk):
    pk = int(pk)
    part = get_object_or_404(ExamPart,id=pk)
    time = part.time * 60
    input = time
    idSP = pk
    giay = input % 60
    phut= input // 60
    context = {
        'profile' : Profile.objects.get(user = request.user),
        'type' : 'skill',
        'input' : input,
        'phut' : phut,
        'giay': giay,
        'idSP' : idSP,        
    }
    part_history = PracticePartHistory(
                student = request.user,
                name = part.name,
                duration = timedelta(minutes=part.time),
                pass_score = part.pass_score,
                part = part,
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
    context['part_history'] = part_history
    return render(request,'pages/student_test_part.html',context)   
#TODO : New test
def new_test(request,pk):
    pk = int(pk)
    exam = get_object_or_404(Exam,id = pk)
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
    context = {
        'profile' : Profile.objects.get(user = request.user)
    }
    return render(request,'pages/student_select_exam_new.html',context)

def exam_n(request,level):
    level_obj = level
    context = {
        'level' : level_obj
    }
    return render(request,'pages/student_exam_N.html',context)

def exam_skill(request):
    if request.session['level'] is None:
        request.session['level'] = ""
    if request.session['skill'] is None:
        request.session['skill'] = ""
    level = request.GET.get("level")
    skill = request.GET.get("skill")
    if level != "" and level is not None:
        request.session['level'] = level
    if skill != "" and skill is not None:
        request.session['skill'] = skill
    print(request.session['level'],request.session['skill'])
    parts = ExamPart.objects.filter(level = request.session['level'],skill = request.session['skill'])
    profile = get_object_or_404(Profile,id = request.user.id)
    print(parts)
    context = {
        'profile' : profile,
        'parts' : parts
    }
    return render(request,'pages/student_select_skill.html',context)

def exam_skill_result(request,pk):
    result = {}
    answers = 'ABCD'
    base_score = {}
    part = get_object_or_404(PracticePartHistory,id = pk)
    value = QuestionHistory.objects.filter(group_question__in = part.groups(),answer__exact = F('correct')).aggregate(sum = Sum('score'))
    total = QuestionHistory.objects.filter(group_question__in = part.groups()).aggregate(sum = Sum('score'))
    value = 0 if value['sum'] is None else value['sum']
    total = 0 if total['sum'] is None else total['sum']
    result[part.name] = value
    base_score[part.name] = total
    part.scored = value
    part.status = True
    part.base_score = total
    part.save()
    profile = Profile.objects.get(user = request.user)    
    context = {
        'result' : result,
        'base_score' : base_score,
        'profile' : profile,
        'part' : part
    }
    return render(request,'pages/student_skill_result.html',context)
    
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

def save_exit_time(request):
    if request.method == 'POST':
        data = json.loads(request.body) #đọc json và lấy dữ liệu từ json
        time = data['exit_time']  
        exti_time = int(time)   
        data_id = data['my_id']
        id = int(data_id)   
 
        duration = datetime.timedelta(seconds=exti_time)
        practice_history = get_object_or_404(PracticePartHistory,id = id)
        practice_history.time_left = duration
        practice_history.save()

        return JsonResponse({'message': 'Success'})  # Phản hồi thành công

def end_time(request):
    if request.method == 'POST':
        data = json.loads(request.body) #đọc json và lấy dữ liệu từ json
        data_id = data['my_id']
        pk = int(data_id) 
        print(pk)
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
        
        response_data = {'redirect_url': reverse('Student:PracticeHistoryDetail', kwargs={'pk': practice_part.practice_history.id})}
        return JsonResponse(response_data)
def history_skill(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    part_list = PracticePartHistory.objects.filter(student = user,practice_history__isnull = True)
    context = {
        'part_list' : part_list,
        'profile' : profile
    }
    return render(request,'pages/student_history_skill.html',context)

@login_required(login_url='jlpt:Login')
@user_passes_test(test_func= JLPT.test_funcs.user_is_student)
def practice_result_detail(request,pk):
    profile = Profile.objects.get(user = request.user)
    practice = get_object_or_404(PracticeHistory,id = pk)
    context = {
        'practice' : practice,
        'profile' : profile
    }
    return render(request,'pages/student_practice_result_detail.html',context)

def skill_result_detail(request,pk):
    profile = Profile.objects.get(user = request.user)
    part = get_object_or_404(PracticePartHistory,id = pk)
    context = {
        'part' : part,
        'profile' : profile
    }
    return render(request,'pages/student_skill_result_detail.html',context)
