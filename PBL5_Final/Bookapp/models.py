from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField('Categories', max_length=100)
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    cover_image = models.ImageField(upload_to='img', blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    recommended_books = models.BooleanField(default=False)
    reading_books = models.BooleanField(default=False)
    grammar_books = models.BooleanField(default=False)
    vocabulary_books = models.BooleanField(default=False)
    listen_books = models.BooleanField(default=False)
    tips_books = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_book