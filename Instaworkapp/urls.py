from django.contrib import admin
from django.urls import path, include
from Instaworkapp import views

app_name = 'Instaworkapp'

urlpatterns = [
    path(r'list/', views.listview, name='listview'),
    path(r'add/', views.addview, name='addview'),
    path(r'edit/<int:id>/', views.editview, name='editview'),
    path(r'delete/<int:id>/', views.deleteview, name='deleteview'),

]