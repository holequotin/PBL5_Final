from django import forms
from .models import BookSearch,Book

class AddBookForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={
    #     'class' : 'form-control col-6',
    #     'id' : 'title-name',
    #     'name' : 'title-name'
    # }))
    # cover_image = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class' : 'form-control',
    #     'id' : 'book-image',
    #     'name' : 'book-image'
    # }))
    # summary = forms.TimeField(widget=forms.Textarea(attrs={
    #     'class' : 'form-control col-6',
    #     'id' : 'title-name',
    #     'name' : 'title-name'
    # }))
    class Meta:
        model = Book
        fields = '__all__'

class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TimeInput(attrs={
        'class':"form-control me-2", 'placeholder': 'Nhập tên sách'
    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book']

