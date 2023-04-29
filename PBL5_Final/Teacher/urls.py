from django.urls import path, include
from .views import *

app_name = 'Teacher'
urlpatterns = [
    path('home',teacher_home,name="TeacherHome"),
    path('exammanager',exam_manager,name = 'ExamManager'),
    path('addexam',teacher_add_exam,name='AddExam'),
    path('delete_exam/<int:pk>',teacher_delete_exam,name = 'DeleteExam'),
    path('detail_exam/<int:pk>',teacher_detail_exam,name = "DetailExam")
]
