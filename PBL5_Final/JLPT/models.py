from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    role = models.CharField(max_length=20,default="student")
    phone_number = models.CharField(max_length=11,default='')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.user.username
