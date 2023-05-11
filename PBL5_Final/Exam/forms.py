from django.forms import models
from .models import *
from django import forms
class AddExamForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-6',
        'id' : 'exam-name',
        'name' : 'exam-name'
    }))
    level = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class' : 'form-control',
        'id' : 'exam-level',
        'name' : 'exam-level'
    }),queryset=Level.objects.all())
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'form-control',
        'id' : 'exam-image',
        'name' : 'exam-image'
    }))
    pass_score = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'id' : 'exam-pass-score',
        'name' : 'exam-pass-score'
    }))
    class Meta:
        model = Exam
        fields = ['name','level','image','pass_score']
        
class AddExamPartForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
    }))
    time = forms.IntegerField(widget = forms.NumberInput(attrs={
        'class' : 'form-control',
    }))
    pass_score = forms.IntegerField(widget = forms.NumberInput(attrs={
        'class' : 'form-control',
        'min' : 0
    }))
    class Meta:
        model = ExamPart
        fields = ['name','time','pass_score']
        
class AddGroupQuesitonForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control'
    # }))
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class' : 'form-control'
    }),required=False)
    class Meta:
        model = GroupQuestion
        fields = ['content','file']
        
class AddQuestionForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.TextInput(attrs={
    #     'class' : 'form-control col-12'
    # }))
    optionA = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-3 options'
    }))
    optionB = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-3 options'
    }))
    optionC = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-3 options'
    }))
    optionD = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-3 options'
    }))
    correct = forms.CharField(widget=forms.Select(choices=[('A','A'),('B','B'),('C','C'),('D','D')],attrs={
        'class' : 'form-control col-6 options'
    }),initial='A')
    score = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control col-6'
    }))
    class Meta:
        model = Question
        fields = ['content','optionA','optionB','optionC','optionD','correct','score']