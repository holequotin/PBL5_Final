from django.urls import path, include
from .views import *

app_name = 'Teacher'
urlpatterns = [
    path('home',teacher_home,name="TeacherHome"),
    path('exammanager/<int:number>',exam_manager,name = 'ExamManager'),
    path('addexam',teacher_add_exam,name='AddExam'),
    path('addexamskill',teacher_add_exam_skill,name='AddExamSkill'),
    path('delete_exam/<int:pk>',teacher_delete_exam,name = 'DeleteExam'),
    path('detail_exam/<int:pk>',teacher_detail_exam,name = "DetailExam"),
    path('add_exam_detail/<int:pk>/',teacher_add_exam_detail,name = "AddExamDetail"),
    path('import/<int:pk>/',importExcel,name='push_excel'),
    path('documentmanager/<int:number>',document_manager,name = 'DocumentManager'),
    path('adddocument',teacher_add_document,name='AddDocument'),
    path('delete_document/<int:pk>',teacher_delete_document,name = 'DeleteDocument'),
    path('detail_document/<int:pk>',teacher_detail_document,name = "DetailDocument"),
    path('profile',teacher_profile,name="TeacherProfile"),

    path('add-exam-skill',add_exam_skill,name = 'AddExamSkill'),
    path('create-exam-skill',create_exam_skill,name = "CreateExamSkill"),
    path('edit-exam-skill/<int:pk>',edit_skill_exam,name='EditExamSkill'),
    path('delete-exam-skill/<int:pk>',delete_exam_skill,name='DeleteExamSkill'),
    path('update-exam-skill/<int:pk>',update_skill_exam,name="UpdateExamSkill"),
    path('skill-manager/<int:number>',exam_skill_manager,name = 'SkillManager'),
    path('add-exam-skill-detail/<int:pk>',add_exam_skill_detail,name='AddExamSkillDetail'),
    path('addbook',teacher_add_book,name='AddBook'),
    path('bookmanager/<int:number>',book_manager,name = 'BookManager'),
    path('delete_book/<int:pk>',teacher_delete_book,name = 'DeleteBook'),
    path('detail_book/<int:pk>',teacher_detail_book,name = "DetailBook"),
    path('import_skill/<int:pk>/',importExcelSkill,name='push_excel_skill'),
    
    path('profile',teacher_profile,name="TeacherProfile"),

]
