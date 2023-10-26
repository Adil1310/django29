from django.contrib import admin
from .models import Student, Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)

# Login: Admin
# Password: 654321