from django.shortcuts import render, redirect
from .models import Teacher, Attendance, Classroom, Student
from .forms import AttendanceForm, StudentForm
from django.utils import timezone
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def classroom_index(request):
    parkour_classes = Classroom.objects.filter(type='Parkour')
    gymnastics_classes = Classroom.objects.filter(type='Gymnastics')
    classrooms = (parkour_classes, gymnastics_classes)
    
    context = {
        'classrooms' : classrooms
    }
    
    return render(request, 'classroom_index.html', context)
    
def classroom_detail(request, pk):
    classroom = Classroom.objects.get(pk=pk)
    students = Student.objects.filter(classroom=classroom)
    student_form = StudentForm(initial={'classroom' : classroom})
    #prevent taking attendance twice in one day:
    attendance = None
    is_attendance_already_taken = False
    todays_attendance = classroom.attendance_set.filter(date=datetime.date.today()).last() or None
    
    if todays_attendance:
        is_attendance_already_taken = True
        attendance = todays_attendance

    context = {
        'classroom' : classroom,
        'students' : students,
        'student_form' : student_form,
        'is_attendance_already_taken': is_attendance_already_taken,
        'attendance' : attendance,
    }
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('classroom_detail', pk=pk)
    
    return render(request, 'classroom_detail.html', context)
    
def student_index(request):
    students = Student.objects.all().order_by('-classroom')
    
    context = {
        'students': students
    }
    
    return render(request, 'student_index.html', context)

def classroom_attendance(request, pk):
    classroom = Classroom.objects.get(pk=pk)
    students = Student.objects.filter(classroom=classroom)
    attendance_form = AttendanceForm(initial = {
        'classroom':classroom,
        'date': timezone.now(),
    })
    attendance_form.fields['students'].queryset = students
    print(attendance_form.fields)
    
    if request.method == 'POST':
        attendance_form = AttendanceForm(request.POST)
        if attendance_form.is_valid():
            attendance_form.save()
            return redirect('classroom_detail', pk=pk)
            
    context = {
        'classroom' : classroom,
        'attendance_form' : attendance_form,
    }

    return render(request, 'classroom_attendance.html', context)

def attendance_edit(request, pk):
    attendance = Attendance.objects.get(pk=pk)
    classroom = attendance.classroom
    students = Student.objects.filter(classroom=classroom)
    attendance_form = AttendanceForm(instance=attendance)
    attendance_form.fields['students'].queryset = students
    
    if request.method == 'POST':
        attendance_form = AttendanceForm(request.POST)
        if attendance_form.is_valid():
            attendance_form.save()
            return redirect('classroom_detail', pk=classroom.pk)
              
    context = {
        'classroom' : classroom,
        'attendance_form' : attendance_form,
    }

    return render(request, 'attendance_edit.html', context)
    
    
    
    