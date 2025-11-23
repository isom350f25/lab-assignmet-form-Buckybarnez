from django.urls import path
from .views import *
 
urlpatterns = [
    path('employeeslist/', employee_list, name='employee_list'),
    path('employee/<int:employee_id>/',employee_detail, name='employee_detail'),
    path('engineers/', employee_engineers, name='employee_engineers'),
    path('employee/add/', employee_create, name='employee_create'),
    path('projects/add/', add_project, name='add_project'),
]

 
