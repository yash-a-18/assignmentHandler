from django.db import models
from manageAssignments.models import Assignment
from RegistrationModule.models import Student

# Create your models here.

class Submission(models.Model):
    assign_id=models.CharField(max_length=10)
    student_email=models.CharField(max_length=50)
    submission_date=models.DateTimeField()
    submission_file_name=models.FileField(max_length=50)
    submission_marks_logic=models.BooleanField(max_length=6)
    submission_marks_uniqueness=models.BooleanField(max_length=6)
    submission_marks_quality=models.BooleanField(max_length=6)
    models.ForeignKey(Assignment,on_delete=models.CASCADE)
    models.ForeignKey(Student,on_delete=models.CASCADE)
    '''to set a composite primary key'''
    class Meta:
        unique_together = ('assign_id', 'student_email')