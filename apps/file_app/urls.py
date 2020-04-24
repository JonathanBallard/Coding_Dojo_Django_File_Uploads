from django.urls import path 
from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    # path('', views.index), 
    path('', views.list, name="list"), 
    path('upload/file/', views.uploadFile), 
    path('upload/', views.upload_file), 
    path('file/', views.showFile), 

] 
