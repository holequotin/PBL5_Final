from django import forms
from Exam.models import *

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = '__all__'

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class ExamPartForm(forms.ModelForm):
    class Meta:
        model = ExamPart
        fields = '__all__'

class GroupQuestionForm(forms.ModelForm):
    class Meta:
        model = GroupQuestion
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'