from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Exam)
admin.site.register(ExamPart)
admin.site.register(GroupQuestion)
admin.site.register(Question)
admin.site.register(Level)