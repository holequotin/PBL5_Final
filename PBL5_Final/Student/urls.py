from django.urls import path,include
from .views import *
from . import views

app_name = 'Student'

urlpatterns = [
    path('index',index,name='StudentHome'),
    path('exam-list/<str:level>',exam_list,name='ExamList'),
    path('exam-detail/<int:pk>',exam_detail,name = 'ExamDetail'),
    path('practice-history-detail/<int:pk>',practice_history_detail,name='PracticeHistoryDetail'),
    path('exam-test-part/<int:pk>',test_part,name='TestPart'),
    path('exam-start-test/<int:pk>',start_test,name = 'StartTest'),
    path('hx-update-answer/<int:pk>',update_answer,name='UpdateAnswer'),
    path('hx-question-history/<int:pk>',question_history_detail,name = 'QuestionHistory'),
    path('exam-list',exam_select_list,name='ExamSelectList'),
    path('exam-list/<str:level>',exam_list,name='ExamList'),
    path('exam<str:level>',exam_n,name='ExamN'),
    path('student-complete-part/<int:pk>',complete_practice_part,name = 'CompletePart'),
    path('student-practice-result/<int:pk>',practice_result,name='PracticeResult'),
    path('student-history-list',history_list,name = 'HistoryList'),
    path('student-new-test/<int:pk>',new_test,name='NewTest'),
    path('save-exit-time/',save_exit_time,name='save_exit_time'),
    path('end-time/',end_time,name = 'EndTime'),
]
