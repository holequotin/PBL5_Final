from django.urls import path, include
from .views import *

app_name = 'Exam'
urlpatterns = [
    path('hx-detail-exam/<int:pk>',detail_exam,name="DetailExam"),
    path('hx-edit-exam/<int:pk>',edit_exam,name="EditExam"),
    path('hx-exam-part-form/<int:pk>',exam_part_form,name='AddExamPartForm'),
    path('hx-group-question-form/<int:pk>',group_question_form,name='AddGroupQuestionForm'),
    path('hx-question-form/<int:pk>',question_form,name='AddQuestionForm'),
    path('hx-exam-part-detail/<int:pk>',exam_part_detail,name='ExamPartDetail'),
    path('hx-question-detail/<int:pk>',question_detail,name='QuestionDetail'),
    path('hx-delete-part/<int:pk>',delete_part,name='DeletePart'),
    path("hx-delete-group-question/<int:pk>", delete_group_question, name="DeleteGroupQuestion"),
    path('hx-delete-form',delete_form,name='DeleteForm'),
    path('hx-exam-list/',exam_list,name = 'ExamList')
]
