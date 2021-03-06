from django.db import models
from RegistrationModule.models import Courses
from RegistrationModule.models import Student
from RegistrationModule.models import Teacher

class Assignment(models.Model):
    #assign_id=models.CharField(max_length=10,primary_key=True)
    assign_id=models.AutoField(primary_key=True)
    assign_name=models.CharField(max_length=50)
    assign_file=models.FileField(upload_to='files/',null=True)
    teacher_email=models.CharField(max_length=50)
    c_id=models.CharField(max_length=10)
    initial_date=models.DateTimeField()
    assign_due_date=models.DateTimeField()
    assign_max_size_kb=models.IntegerField()
    models.ForeignKey(Courses,on_delete=models.CASCADE)
    models.ForeignKey(Teacher,on_delete=models.CASCADE)
    def __str__(self):
        return self.assign_name