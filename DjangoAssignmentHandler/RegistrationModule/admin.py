from django.contrib import admin
from RegistrationModule.models import Student,Teacher,Courses,AppUsers,StudentCourse

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Courses)
admin.site.register(AppUsers)
admin.site.register(StudentCourse) 
