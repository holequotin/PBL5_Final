from django.urls import path, include
from .views import *

app_name = 'Teacher'
urlpatterns = [
    path('home',teacher_home,name="TeacherHome"),
    path('exammanager/<int:number>',exam_manager,name = 'ExamManager'),
    path('addexam',teacher_add_exam,name='AddExam'),
    path('delete_exam/<int:pk>',teacher_delete_exam,name = 'DeleteExam'),
    path('detail_exam/<int:pk>',teacher_detail_exam,name = "DetailExam"),
    path('add_exam_detail/<int:pk>/',teacher_add_exam_detail,name = "AddExamDetail"),
    path('import/<int:pk>/',importExcel,name='push_excel'),
    path('documentmanager/<int:number>',document_manager,name = 'DocumentManager'),
    path('adddocument',teacher_add_document,name='AddDocument'),
    path('delete_document/<int:pk>',teacher_delete_document,name = 'DeleteDocument'),
    path('detail_document/<int:pk>',teacher_detail_document,name = "DetailDocument"),

    path('addbook',teacher_add_book,name='AddBook'),
    path('bookmanager/<int:number>',book_manager,name = 'BookManager'),
    path('delete_book/<int:pk>',teacher_delete_book,name = 'DeleteBook'),
    path('detail_book/<int:pk>',teacher_detail_book,name = "DetailBook"),
    path('detail_book/<int:pk>',teacher_detail_book,name = "DetailBook"),
]
