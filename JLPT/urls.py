from django.urls import path, include
from .views import *

app_name = 'jlpt'
urlpatterns = [
    path('login/',login_page,name='Login'),
    path('register/',register_page,name='Register'),
    path('teacherhome/',teacher_home,name = 'TeacherHome'),
    path('logout/',login_page,name='Logout')
]
