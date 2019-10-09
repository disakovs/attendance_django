from django.db import models

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
     
class Teacher(NamableModel, models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    

class Attendance(models.Model):
    students = models.ManyToManyField('Student', related_name='attendances')
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=created_on)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    
    