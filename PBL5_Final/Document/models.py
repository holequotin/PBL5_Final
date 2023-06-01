from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True)
    def __str__(self):
        return self.title

