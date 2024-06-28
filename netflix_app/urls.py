from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_content', views.add_content, name='add_content'),
    path('salary_checker', views.salary_checker, name='salary_checker'),
]