from django.urls import path, include
from .views import *
from . import views
app_name = 'Bookapp'
urlpatterns = [
   path('home/',views.home, name='home'),
   path('all_books', views.all_books, name='all_books'),
   path('genre/<str:slug>', views.category_detail, name='category_detail'),
   path('book/<str:slug>', views.book_detail, name='book_detail'),
   path('search_books', views.search_book, name='book_search'),
   path('hx-book-list/<int:number>',book_list,name = 'BookList'),
   path('hx-edit-book/<int:pk>',edit_book,name="EditBook"),
]