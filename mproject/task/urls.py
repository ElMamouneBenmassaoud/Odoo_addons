from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('addTask/', views.addTask, name='addTask'),

]