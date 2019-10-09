from django import forms
from .models import Classroom, Teacher, Attendance, Student

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'classroom', 'teacher', 'students',]
        
        widgets = {
                'classroom': forms.HiddenInput(),
                'date' : forms.SelectDateWidget(),
                'students' : forms.CheckboxSelectMultiple(),
        }
        
        # def __init__(self, classroom, *args, **kwargs):
        #     super(AttendanceForm, self).__init__(*args, **kwargs)
        #     self.fields['students'].queryset = Student.objects.filter(classroom=classroom)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'classroom']
        widgets = {'classroom': forms.HiddenInput()}