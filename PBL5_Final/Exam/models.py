from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
import os
from enum import Enum
# Create your models here.

CATEGORY_CHOICES = [
    ('Listening','Listening'),
    ('Reading','Reading'),
    ('Grammar','Grammar'),
    ('Vocabulary','Vocabulary'),
]
LEVELS_CHOICES = [
    ('N1','N1'),
    ('N2','N2'),
    ('N3','N3'),
    ('N4','N4'),
    ('N5','N5'),
]

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Level(models.Model):
    name =  models.CharField(unique=True,max_length=100)
    
    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(unique=True,max_length=100)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',default='media/jlpt.jpeg',storage=fs)
    pass_score = models.IntegerField(default=0)
    
    def parts(self):
        return ExamPart.objects.all().filter(exam = self)
    # def delete(self, *args, **kwargs):
    #     if os.path.isfile(self.image.path):
    #         os.remove(self.image.path)
    #     return super().delete(*args, **kwargs)
    
    
class ExamPart(models.Model):
    user = models.ForeignKey(User,null = True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.PositiveIntegerField()
    pass_score = models.PositiveIntegerField(default=0)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True,blank=True)
    skill = models.CharField(max_length=100,null=True,blank=True,choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=100,null=True,blank=True,choices=LEVELS_CHOICES)
    
    def groups(self):
        return GroupQuestion.objects.all().filter(exam_part = self)
    def __str__(self) -> str:
        return self.name

class GroupQuestion(models.Model):
    exam_part = models.ForeignKey(ExamPart,on_delete=models.CASCADE)
    content = RichTextField(null=True,blank=True)
    file = models.FileField(upload_to='media/',null=True, blank=True)
    #audio = models.FileField(upload_to='media/', null=True, blank=True)
    def questions(self):
        return Question.objects.all().filter(group_question = self)
    
class Question(models.Model):
    group_question = models.ForeignKey(GroupQuestion, on_delete= models.CASCADE)
    content = RichTextField(null=True,blank=True)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    score = models.IntegerField()
    correct = models.CharField(max_length=1,default="A")
    #test