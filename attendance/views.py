from django.shortcuts import render, redirect
from .models import Teacher, Attendance, Classroom, Student
from .forms import AttendanceForm, StudentForm
from django.utils import timezone
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.views.generic import View
from django.http import HttpResponse
#messages
from django.contrib import messages
# Create your views here.
class DashboardTemplateView(TemplateView):
    template_name= 'attendance/home.html'

class ClassroomDetail(LoginRequiredMixin, ModelFormMixin, DetailView):
    model = Classroom
    form_class = StudentForm
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        last_attendance = self.object.attendance_set.last()

        context['student_form'] = StudentForm(initial={'classroom' : context['classroom']}) #self.get_form()
        context['students'] = context['classroom'].student_set.all()
        context['last_attendance'] = last_attendance

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST)
        
        if form.is_valid():
            return self.form_valid(form)
        else: 
            return self.form_invalid(form)
        
    def get_success_url(self, **kwargs):
        messages.success(self.request, "Student created!")
        print('type', type(self.object.classroom_id), self.object.classroom_id)
        return reverse('classroom_detail', kwargs = {'pk': self.object.classroom_id })

class ClassroomListView(ListView):
    model = Classroom
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        parkour_classes = Classroom.objects.filter(type='Parkour')
        gymnastics_classes = Classroom.objects.filter(type='Gymnastics')
        all_classes = [parkour_classes, gymnastics_classes]
        
        context['all_classes'] = all_classes
        
        return context

class StudentListView(ListView):
    model = Student
    ordering = ['first_name', 'last_name']

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'att/student_form.html'
    fields = ['first_name', 'last_name', 'classroom']
    
    def get_success_url(self):
        messages.success(self.request, "Student created!")
        return reverse('classroom_list')
        
class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'attendance/student_form.html'
    fields = ['first_name', 'last_name', 'classroom']
    
    def get_success_url(self):
        return reverse('student_index')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'attendance/student_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('student_index')

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'attendance/classroom_attendance.html'
    form_class = AttendanceForm
    
    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        
        classroom = Classroom.objects.get(pk=self.kwargs['pk'])       
        initial['classroom'] = classroom
        initial['date'] = timezone.now()
        
        return initial
     
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        classroom = Classroom.objects.get(pk=self.kwargs['pk'])

        form.fields['students'].queryset = Student.objects.filter(classroom=classroom)
        return form
        
    def get_success_url(self):
        print('self kwargs:  ', self.kwargs)
        return reverse('classroom_detail', kwargs = {'pk': self.kwargs['pk'] })

class AttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendance/attendance_edit.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        classroom = Classroom.objects.get(pk=context['object'].classroom_id)
        context['classroom'] = classroom 
        
        return context
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        
        classroom = self.object.classroom
        form.fields['students'].queryset = classroom.student_set
        
        return form
    
    def get_success_url(self):
        classroom = self.object.classroom
        return reverse('classroom_detail', kwargs = {'pk': classroom.pk})


    
    
    
    