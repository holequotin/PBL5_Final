from django.urls import path,include
from .views import *
app_name = 'Student'

urlpatterns = [
    path('index',index,name='StudentHome'),
    path('exam-list/<str:level>',exam_list,name='ExamList'),
    path('exam-detail/<int:pk>',exam_detail,name = 'ExamDetail'),
    path('exam-test-part/<int:pk>',test_part,name='TestPart'),
    path('exam-start-test/<int:pk>',start_test,name = 'StartTest')
]
