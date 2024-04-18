from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_list),
    path('student/<int:id>', views.student_info),

]

