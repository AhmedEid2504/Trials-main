from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('students/', views.students_list),
    path('student/<int:id>', views.student_info),

]

