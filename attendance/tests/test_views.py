from django.test import TestCase
from django.urls import reverse
from attendance.models import Student, Classroom, Teacher, Attendance
from attendance.forms import AttendanceForm, StudentForm
from django.utils import timezone
from datetime import date
from django.test import Client
# Create your tests here.

class ClassroomViewTestCase(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')
    
    def test_list_view_logged_out(self):
        obj = self.classroom
        list_url = reverse("classroom_list")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)
    
    def test_detail_view_logged_out(self):
        obj = self.classroom
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 302)

class StudentSearchViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')
        student1 = Student.objects.create(first_name='Bill', last_name='Kill', classroom=classroom)
        student2 = Student.objects.create(first_name='Another', last_name='Kill', classroom=classroom)
        teacher = Teacher.objects.create(first_name='First', last_name='Last')
    
    def test_student_search_valid(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('student_search'),
            filter='q',
            value='parkour')
        response = self.client.get(url)
        self.assertEqual(response.context['object_list'].count(), 2)
    
    def test_student_search_empty_string(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('student_search'),
            filter='q',
            value='')
        response = self.client.get(url)
        self.assertEqual(response.context['object_list'].count(), 2)
    
    def test_student_search_valid_partial_return(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('student_search'),
            filter='q',
            value='bill')
        response = self.client.get(url)
        self.assertEqual(response.context['object_list'].count(), 1)
    
    def test_student_search_nothing_found(self):
        url = '{url}?{filter}={value}'.format(
            url=reverse('student_search'),
            filter='q',
            value='kram')
        response = self.client.get(url)
        self.assertEqual(response.context['object_list'].count(), 0)