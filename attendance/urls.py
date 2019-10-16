from django.urls import path
from . import views

from django.views.generic.base import TemplateView
from .views import StudentListView, DashboardTemplateView, ClassroomDetail, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', views.DashboardTemplateView.as_view(), name='home'),
    path('classes/', views.ClassroomListView.as_view(), name='classroom_list'),
    path('classes/<int:pk>/', views.ClassroomDetail.as_view(), name='classroom_detail'),
    path('students/<int:pk>/edit', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete', views.StudentDeleteView.as_view(), name='student_delete'),
    path('students/', views.StudentListView.as_view(), name='student_index'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('attendance/<int:pk>/edit/', views.AttendanceUpdateView.as_view(), name='attendance_edit'),
    path('classes/<int:pk>/attendance/', views.AttendanceCreateView.as_view(), name='class_attendance'),
]