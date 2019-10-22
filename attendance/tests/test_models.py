from django.test import TestCase
from attendance.models import Student, Classroom, Teacher, Attendance
from django.utils import timezone
from datetime import date
# Create your tests here.
class AttendanceModelTestCase(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')
        student1 = Student.objects.create(first_name='Bill', last_name='Kill', classroom=self.classroom)
        student2 = Student.objects.create(first_name='Another', last_name='Kill', classroom=self.classroom)
        teacher = Teacher.objects.create(first_name='First', last_name='Last')

        self.attendance = Attendance.objects.create(classroom=self.classroom, teacher=teacher, created_on=timezone.now(), date='2019-10-19')       
        self.attendance.students.add(student1)
        self.attendance.students.add(student2)
    
    def test_qs(self):
        self.assertEqual(self.attendance.students.count(), 2)

class ClassroomModelTestCase(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(type='Parkour', age_limit='5-7', name='Parkour Ninja')
        self.teacher = teacher = Teacher.objects.create(first_name='First', last_name='Last')
    
    def test_attendance_not_taken(self):
        self.assertFalse(self.classroom.is_attendance_taken_today())
    
    def test_attendance_taken_today(self):
        Attendance.objects.create(classroom=self.classroom, teacher=self.teacher, created_on=timezone.now(), date=date.today())
        self.assertTrue(self.classroom.is_attendance_taken_today())