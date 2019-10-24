from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse
from attendance.models import Student, Classroom, Teacher, Attendance
from attendance.views import (ClassroomDetail, StudentListView, StudentUpdateView, 
                               StudentDeleteView, AttendanceUpdateView, 
                               AttendanceCreateView,)
from attendance.forms import AttendanceForm, StudentForm
from django.utils import timezone
from datetime import date
from django.test import Client
# Create your tests here.
User = get_user_model()

class ClassroomViewAuthTestCase(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(
                    username='abc23444',
                    password='passwordtest123',
                    )
    
    def test_detail_view(self):
        obj = self.classroom
        self.client.force_login(self.user)
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 200)
    
    def test_detail_view_with_factory(self):
        obj = self.classroom
        request = self.factory.get(obj.get_absolute_url())
        request.user = self.user
        response = ClassroomDetail.as_view()(request, pk=obj.id)
        self.assertEqual(response.status_code, 200)
        
class StudentViewAuthTestCase(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')
        self.student = Student.objects.create(first_name="Bob", last_name="Test", classroom=self.classroom)
        self.factory = RequestFactory()
        self.data = {'first_name' : "Changed", 'last_name' : "new", "classroom" : self.classroom.id}
        self.user = User.objects.create(
                    username='abc23444',
                    password='passwordtest123',
                    )
                    
    def test_student_list_view_logged_out(self):
        list_url = reverse('student_index')
        request = self.factory.get(list_url)
        response = StudentListView.as_view()(request)
        
        self.assertEqual(response.status_code, 200)
        
    def test_student_update_view(self):
        student_edit_url = reverse("student_edit", kwargs = {'pk': str(self.student.id)})
        request = self.factory.post(student_edit_url, data=self.data)
        request.user = self.user
        response = StudentUpdateView.as_view()(request, pk=self.student.id)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.get(pk=1).first_name, "Changed")
        
    def test_student_delete_view(self):
        student_delete_url = reverse("student_delete", kwargs = {'pk': str(self.student.id)})
        request = self.factory.post(student_delete_url)
        request.user = self.user
        response = StudentDeleteView.as_view()(request, pk=self.student.id)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.count(), 0)

class AttendanceViewAuthTestCase(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')
        self.student1 = Student.objects.create(first_name="Bob", last_name="Test", classroom=self.classroom)
        self.student2 = Student.objects.create(first_name='Another', last_name='Kill', classroom=self.classroom)
        self.factory = RequestFactory()

        self.user = User.objects.create(
                    username='abc23444',
                    password='passwordtest123',
                    )
                    
    def test_student_attendance_create_view(self):
        attendance_url = reverse('class_attendance', kwargs = {'pk': str(self.classroom.id)})
        request = self.factory.get(attendance_url)
        request.user = self.user
        response = AttendanceCreateView.as_view()(request, pk=self.classroom.id)
        
        self.assertEqual(response.status_code, 200)
        
    # def test_student_update_view(self):
    #     student_edit_url = reverse("student_edit", kwargs = {'pk': str(self.student.id)})
    #     request = self.factory.post(student_edit_url, data=self.data)
    #     request.user = self.user
    #     response = StudentUpdateView.as_view()(request, pk=self.student.id)
    #     
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Student.objects.get(pk=1).first_name, "Changed")
    #     
    # def test_student_delete_view(self):
    #     student_delete_url = reverse("student_delete", kwargs = {'pk': str(self.student.id)})
    #     request = self.factory.post(student_delete_url)
    #     request.user = self.user
    #     response = StudentDeleteView.as_view()(request, pk=self.student.id)
    #     
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Student.objects.count(), 0)