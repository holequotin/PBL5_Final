from django.urls import path, include
from .views import *

app_name = 'Exam'
urlpatterns = [
    path('hx-detail-exam/<int:pk>',detail_exam,name="DetailExam"),
    path('hx-edit-exam/<int:pk>',edit_exam,name="EditExam")
]
