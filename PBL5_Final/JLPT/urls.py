from django.urls import path, include
from .views import *

app_name = 'jlpt'
urlpatterns = [
    path('login/',login_page,name='Login'),
    path('register/',register_page,name='Register')
]
