from django import forms
from .models import BookSearch,Book,Category
from django.utils.text import slugify

class AddBookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control col-6',
        'id': 'title-name',
        'name': 'title-name'
    }))
    cover_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'id': 'book-image',
        'name': 'book-image'
    }))
    summary = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control col-6',
        'id': 'summary',
        'name': 'summary'
    }))
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={
    'class': 'form-control col-6',
    'id': 'category-name',
    'name': 'category-name'
    }))


    pdf = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'id': 'book-pdf',
        'name': 'book-pdf'
    }))
    recommended_books = forms.BooleanField(required=False)
    reading_books = forms.BooleanField(required=False)
    grammar_books = forms.BooleanField(required=False)
    vocabulary_books = forms.BooleanField(required=False)
    listen_books = forms.BooleanField(required=False)
    tips_books = forms.BooleanField(required=False)

    class Meta:
        model = Book
        fields = ['title', 'cover_image', 'summary', 'category', 'pdf', 'recommended_books','reading_books', 'grammar_books', 'vocabulary_books', 'listen_books', 'tips_books']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)  # Tự động điền giá trị slug từ title
        if commit:
            instance.save()
        return instance



class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TimeInput(attrs={
        'class':"form-control me-2", 'placeholder': 'Nhập tên sách'
    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book']

