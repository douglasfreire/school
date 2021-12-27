from django.contrib import admin
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.cachefiles import ImageCacheFile
from imagekit.processors import ResizeToFill

from usersregistration.form import EmployeeSchoolForm, StudentSchoolForm
from usersregistration.models import SchoolEmployee, Student


class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(100, 60)]
    # format = 'JPEG'
    options = {'quality': 60 }


def cached_admin_thumb(instance):
    cached = ImageCacheFile(AdminThumbnailSpec(instance.photo))
    print("cached", cached)
    cached.generate()
    return cached

class EmployeeSchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf", "rg", "phone")
    form = EmployeeSchoolForm

class StudentSchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf", "rg", "phone", "emergency_contact_name", "emergency_contact_phone", "admin_thumbnail")
    form = StudentSchoolForm
    admin_thumbnail = AdminThumbnail(image_field=cached_admin_thumb)
    
    admin_thumbnail.short_description = 'Photo'
    admin_thumbnail.allow_tags = True



admin.site.register(SchoolEmployee, EmployeeSchoolAdmin)
admin.site.register(Student, StudentSchoolAdmin)