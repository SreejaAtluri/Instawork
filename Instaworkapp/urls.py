from django.contrib import admin
from django.urls import path, include
from Instaworkapp import views
from Instaworkapp.views import AdddataListView, AdddataCreateView, AdddataUpdateView, AdddataDeleteView

app_name = 'Instaworkapp'

urlpatterns = [
    path(r'', AdddataListView.as_view(), name='listview'),
    # path(r'add/', views.addview, name='addview'),
    path(r'add/', AdddataCreateView.as_view(), name='addview'),
    path(r'update/<int:id>/', AdddataUpdateView.as_view(), name='updateview'),
    path(r'delete/<int:id>/', AdddataDeleteView.as_view(), name='deleteview'),

]