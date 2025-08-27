from django.urls import path
from . import views

urlpatterns = [
    # Students
    path('students/', views.list_student),
    path('students/add/', views.add_student),
    path('students/delete/<int:id>/', views.delete_student),

    # Subjects
    path('subjects/', views.list_subjects),
    path('subjects/add/', views.add_subject),
    path('subjects/delete/<int:id>/', views.delete_subject),

    # Grades
    path('grades/add/', views.add_grade),
   # path('grades/<int:student_id>/', views.list_student),
    path('grades/average/<int:student_id>/', views.average_student),]