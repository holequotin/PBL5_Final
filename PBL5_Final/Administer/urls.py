from django.urls import path, include
from .views import *

app_name = 'Administer'
urlpatterns = [
    path('teacher/',administer_teacher,name='Teacher'),
    path('student/',administer_student,name='Student'),
    path('exam/',administer_exam,name='Exam'),
    path('practice-history/',administer_practice_history,name='PracticeHistory'),
    path('document/',administer_document,name='Document'),
    path('book/',administer_book,name='Book'),
]
