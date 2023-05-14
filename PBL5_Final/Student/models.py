from django.db import models
from Exam.models import *
from django.contrib.auth.models import User
from Exam.models import *
# Create your models here.
class PracticeHistory(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'Student')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=100)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/history',default='media/jlpt.jpeg',storage=fs)
    pass_score = models.IntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = False) 
    
    def parts(self):
        return PracticePartHistory.objects.all().filter(practice_history = self)

class PracticePartHistory(models.Model):
    name = models.CharField( max_length=100)
    duration = models.DurationField() # sử dụng timedelta để nhập dữ liệu
    pass_score = models.IntegerField(default=0)
    practice_history = models.ForeignKey(PracticeHistory,on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    time_left = models.DurationField()
    
    def groups(self):
        return GroupQuestionHistory.objects.all().filter(part = self)
    
class GroupQuestionHistory(models.Model):
    part = models.ForeignKey(PracticePartHistory,on_delete=models.CASCADE)
    content = RichTextField(null=True,blank=True)
    file = models.FileField(upload_to='media/history',null=True, blank=True)
    
    def questions(self):
        return QuestionHistory.objects.all().filter(group_question = self)
    
class QuestionHistory(models.Model):
    group_question = models.ForeignKey(GroupQuestionHistory, on_delete= models.CASCADE)
    content = RichTextField(null=True,blank=True)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    score = models.IntegerField()
    correct = models.CharField(max_length=1,default="A")
    answer = models.CharField(max_length=1,default="A",null = True,blank = True)