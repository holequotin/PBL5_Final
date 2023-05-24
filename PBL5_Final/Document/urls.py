from django.urls import path, include
from .views import *
from . import views
app_name = 'Document'
urlpatterns = [
   path('document/',views.list, name='test'),
   path('hx-document-list/<int:number>',document_list,name = 'DocumentList'),
   path('hx-edit-document/<int:pk>',edit_document,name="EditDocument"),
    path('detail_document/<int:pk>',document_detail,name = "DetailDocument"),
   
]