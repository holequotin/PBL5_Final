from django.urls import path, include
from .views import *

app_name = 'Exam'
urlpatterns = [
    path('hx-detail-exam/<int:pk>',detail_exam,name="DetailExam"),
    path('hx-edit-exam/<int:pk>',edit_exam,name="EditExam"),
    path('hx-exam-part-form/<int:pk>',exam_part_form,name='AddExamPartForm'),
    path('hx-group-question-form/<int:pk>',group_question_form,name='AddGroupQuestionForm'),
    path('hx-update-group-question/<int:pk>',update_group_question,name='UpdateGroupQuestion'),
    path('hx-question-form/<int:pk>',question_form,name='AddQuestionForm'),
    path('hx-update-answer/<int:pk>',update_answer,name='UpdateAnswer'),
    path('hx-exam-part-detail/<int:pk>',exam_part_detail,name='ExamPartDetail'),
    path('hx-question-detail/<int:pk>',question_detail,name='QuestionDetail'),
    path('hx-delete-part/<int:pk>',delete_part,name='DeletePart'),
    path("hx-delete-group-question/<int:pk>", delete_group_question, name="DeleteGroupQuestion"),
    path('hx-delete-form',delete_form,name='DeleteForm'),
    path("hx-delete-question/<int:pk>", delete_question, name="DeleteQuestion"),
    path('hx-exam-list/<int:number>',exam_list,name = 'ExamList'),
    path('hx-skill-list/<int:number>',skill_list,name = 'SkillList'),
    path('hx-update-question-content/<int:pk>',update_question_content,name = 'UpdateQuestionContent'),
    path('hx-update-question-form/<int:pk>',update_question_form,name = 'UpdateQuestionForm'),
    path('hx-add-group-skill/<int:pk>',group_skill_form,name = 'AddGroupSkillForm'),
    path('hx-add-question-skil/<int:pk>',question_skill_form,name = 'AddQuestionSkillForm'),
    path('hx-update-group-skill/<int:pk>',update_group_skill,name='UpdateGroupSkill'),
    path('hx-update-question-skill/<int:pk>',update_question_skill_form,name = 'UpdateQuestionSkillForm')
]
