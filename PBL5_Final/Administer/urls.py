from django.urls import path, include
from .views import *

app_name = 'Administer'
urlpatterns = [
    path('teacher/',administer_teacher,name='Teacher'),
    path('student/',administer_student,name='Student'),
    path('exam/',administer_exam,name='Exam'),
    path('practice-history/',administer_practice_history,name='PracticeHistory'),
    path('hx-document/<int:number>',administer_document,name='Document'),
    path('book/',administer_book,name='Book'),
    path('hx-teacher-table',search_teacher,name='TeacherTable'),
    path('hx-edit-teacher-form/<int:pk>',edit_teacher,name = 'EditTeacher'),
    path('hx-edit-student-form/<int:pk>',edit_student,name='EditStudent'),
    path('update-teacher/<int:pk>',update_teacher,name = 'UpdateTeacher'),
    path('update-student/<int:pk>',update_student,name='UpdateStudent'),
    path('delete-teacher/<int:pk>',delete_teacher,name='DeleteTeacher'),
    path('delete-student/<int:pk>',delete_student,name='DeleteStudent'),
    path('reset-password/<int:pk>',reset_password,name='ResetPassword')
]
