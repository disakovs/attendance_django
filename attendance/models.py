from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class NamableModel:
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return self.full_name()

class Student(NamableModel, models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['first_name', 'last_name']

    
class Classroom(models.Model):
    CLASS_CHOICES = (
        ('Parkour Ages 5-7', 'Ninja Parkour'),
        ('Parkour Ages 6-10', 'Pee Wee Parkour'),
        ('Gymnastics Ages 2-3', 'Little Rabits'),
        ('Gymnastics Ages 4-5', 'Little Kangaroos'),
        ('Gymnastics Ages 6-10', 'Level 1&2'),
    )
    CLASS_TYPE = (
        ('Parkour', 'Parkour'),
        ('Gymnastics', 'Gymnastics')
    )

    name = models.CharField(
        max_length=50,
        choices = CLASS_CHOICES,
    )
    age_limit = models.CharField(max_length=50)
    type = models.CharField(
        max_length=20,
        choices = CLASS_TYPE
    )
     
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('classroom_detail', args=(str(self.pk)))
    
    def is_attendance_taken_today(self):
        "returns boolean value depending on if attendance was taken that day for a particular class"
        qs = self.attendance_set.all()
        if qs:
            today_attendance = qs.get(date=date.today())
            if today_attendance:
                return True
        
        return False
        
class Teacher(NamableModel, models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    

class Attendance(models.Model):
    students = models.ManyToManyField('Student', related_name='attendances')
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=created_on)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    
    #def is_attendance_already_taken_for_this_class_today(self):
    #    Classroom.objects.get(classroom=self.classroom).attendance_set.get(date=date.today())
    