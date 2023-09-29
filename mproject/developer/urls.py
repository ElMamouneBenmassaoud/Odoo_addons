from django.urls import path
from .views import DevDetailVue, IndexView
from . import views

app_name = 'developer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', DevDetailVue.as_view(), name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),

    path('addTask/<int:pk>', views.addTask, name='addTask'),

]