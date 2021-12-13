from django.contrib import admin
from usersregistration.form import EmployeeSchoolForm, StudentSchoolForm

from usersregistration.models import SchoolEmployee, Student

class EmployeeSchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf", "rg", "phone")
    form = EmployeeSchoolForm

class StudentSchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf", "rg", "phone", "emergency_contact_name", "emergency_contact_phone")
    form = StudentSchoolForm


admin.site.register(SchoolEmployee, EmployeeSchoolAdmin)
admin.site.register(Student, StudentSchoolAdmin)