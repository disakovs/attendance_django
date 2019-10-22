from django.test import TestCase
from django.urls import reverse
from attendance.models import Student, Classroom, Teacher, Attendance
from attendance.forms import AttendanceForm, StudentForm
from django.utils import timezone
from datetime import date
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