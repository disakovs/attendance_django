from django.test import TestCase
from attendance.models import Student, Classroom, Teacher, Attendance
from attendance.forms import AttendanceForm, StudentForm
from django.utils import timezone
from datetime import date
# Create your tests here.

class StudentFormTestCase(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')

    def test_valid_form(self):
        first_name = "Kill"
        last_name = "Bills"
        classroom = self.classroom
        data = {'first_name': first_name, 'last_name':last_name, 'classroom':str(classroom.id)}
        form = StudentForm(data=data)
        
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('first_name'), first_name)