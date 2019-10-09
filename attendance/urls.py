from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classes/', views.classroom_index, name='classroom_index'),
    path('classes/<int:pk>/', views.classroom_detail, name='classroom_detail'),
    path('classes/<int:pk>/attendance/', views.classroom_attendance, name='class_attendance'),
    path('students/', views.student_index, name='student_index'),
    path('attendance/<int:pk>/edit/', views.attendance_edit, name='attendance_edit'),
]