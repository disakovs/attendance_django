import django_filters
from .models import Classroom, Teacher, Attendance, Student
from django import forms

class AttendanceFilter(django_filters.FilterSet):
    WEEKDAY_CHOICES = (
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
    (5, 'Thursday'),
    (6, 'Friday'),
    (7, 'Saturday'),
    )
    
    
    weekday = django_filters.MultipleChoiceFilter(field_name='date', lookup_expr="week_day", choices=WEEKDAY_CHOICES, label="Day of the week", widget=forms.CheckboxSelectMultiple)
    date = django_filters.DateFilter(widget=forms.SelectDateWidget())
    date_range = django_filters.DateRangeFilter(field_name='date', label='Recent Attendances')
    class Meta:
        model = Attendance
        fields = ['date', 'weekday', 'date_range', 'classroom',]
