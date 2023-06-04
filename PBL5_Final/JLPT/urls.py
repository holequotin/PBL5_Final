from django.urls import path, include
from .views import *

app_name = 'jlpt'
urlpatterns = [
    path('login/',login_page,name='Login'),
    path('register/',register_page,name='Register'),
    path('teacherhome/',teacher_home,name = 'TeacherHome'),
    path('logout/',login_page,name='Logout'),
    path('user-info/',user_info,name='UserInfo'),
    path('update-profile',update_profile,name = 'UpdateProfile'),
    path('change-password/',change_password,name='ChangePassword'),
    path('update-password/',update_password,name = "UpdatePassword")
]
