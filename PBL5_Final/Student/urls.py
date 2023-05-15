from django.urls import path,include
from .views import *
app_name = 'Student'

urlpatterns = [
    path('index',index,name='StudentHome'),
    path('exam-list',exam_select_list,name='ExamSelectList'),
    path('exam-list/<str:level>',exam_list,name='ExamList'),
    path('exam<str:level>',exam_n,name='ExamN')
]
