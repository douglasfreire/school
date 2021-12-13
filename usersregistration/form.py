from django import forms
from django.db.models import fields

from usersregistration.models import SchoolEmployee, Student

class EmployeeSchoolForm(forms.ModelForm):
    
    class Meta:
        model = SchoolEmployee
        fields = '__all__'


class StudentSchoolForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'