from django.forms import models
from .models import *
from django import forms

class AddDocumentForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-6',
        'id' : 'title-name',
        'name' : 'title-name'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'form-control',
        'id' : 'document-image',
        'name' : 'document-image'
    }))
    class Meta:
        model = Post
        fields = ['title','body','image']