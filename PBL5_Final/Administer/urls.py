from django.urls import path, include
from .views import *

app_name = 'Administer'
urlpatterns = [
    path('teacher/',administer_teacher,name='Teacher'),
    path('student/',administer_student,name='Student'),
    path('exam/<int:number>',administer_exam,name='Exam'),
    path('practice-history/',administer_practice_history,name='PracticeHistory'),
    path('hx-document/<int:number>',administer_document,name='Document'),
    path('book/',administer_book,name='Book'),
    path('hx-teacher-table',search_teacher,name='TeacherTable'),
    path('hx-student-table',search_student,name='StudentTable'),
    path('hx-edit-teacher-form/<int:pk>',edit_teacher,name = 'EditTeacher'),
    path('hx-edit-student-form/<int:pk>',edit_student,name='EditStudent'),
    path('update-teacher/<int:pk>',update_teacher,name = 'UpdateTeacher'),
    path('update-student/<int:pk>',update_student,name='UpdateStudent'),
    path('delete-teacher/<int:pk>',delete_teacher,name='DeleteTeacher'),
    path('delete-student/<int:pk>',delete_student,name='DeleteStudent'),
    path('reset-password/<int:pk>',reset_password,name='ResetPassword'),
    path('new-document-page/<int:number>',new_document_page,name = 'NewDocumentPage'),
    path('new-exam-page/<int:number>',new_exam_page,name = 'NewExamPage'),
    path('hx-add-teacher-form/',add_teacher_form,name = 'AddTeacherForm'),
    path('create-teacher/',create_teacher,name='CreateTeacher'),
    path('delete_document/<int:pk>',delete_document,name='DeleteDocument'),
    path('delete_book/<int:pk>',delete_book,name='DeleteBook'),
    path('delete_exam/<int:pk>',delete_exam,name='DeleteExam'),

]