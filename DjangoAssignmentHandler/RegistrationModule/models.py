from django.db import models

# Create your models here.
class Student(models.Model):
    '''class for student db'''
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=100)
    dob=models.DateTimeField('date published')
    semester=models.IntegerField()#.CharField(max_length=100)
    course=models.CharField(max_length=10)
    stu_email=models.CharField(max_length=50,primary_key=True)
    address=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=7)
    mobile_no=models.CharField(max_length=15)
    id_no=models.CharField(max_length=15)
    image=models.ImageField(upload_to='stu_pics')
    models.DateTimeField()
    
class Teacher(models.Model):
    '''db table for teachers'''
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=100)
    dob=models.DateTimeField('date published')
    course=models.CharField(max_length=10)
    teach_email=models.CharField(max_length=50,primary_key=True)
    address=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=7)
    mobile_no=models.CharField(max_length=15)
    id_no=models.CharField(max_length=15)
    image=models.ImageField(upload_to='teacher_pics')
    models.DateTimeField()

class Courses(models.Model):
    c_id=models.CharField(max_length=10,primary_key=True)
    c_name=models.CharField(max_length=20)
    c_credit=models.DecimalField(decimal_places=2,max_digits=5)

class Assignment(models.Model):
    assign_id=models.CharField(max_length=10,primary_key=True)
    assign_name=models.CharField(max_length=50)
    teach_email=models.CharField(max_length=50)
    c_id=models.CharField(max_length=10)
    initial_date=models.DateTimeField()
    due_date=models.DateTimeField()
    max_size_kb=models.IntegerField()
    models.ForeignKey(Courses,on_delete=models.CASCADE)
    models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Submission(models.Model):
    assign_id=models.CharField(max_length=10)
    stu_email=models.CharField(max_length=50)
    subm_date=models.DateTimeField()
    file_name=models.CharField(max_length=50)
    marks_logic=models.BooleanField(max_length=6)
    marks_uniqueness=models.BooleanField(max_length=6)
    marks_quality=models.BooleanField(max_length=6)
    models.ForeignKey(Assignment,on_delete=models.CASCADE)
    models.ForeignKey(Student,on_delete=models.CASCADE)
    '''to set a composite primary key'''
    class Meta:
        unique_together = ('assign_id', 'stu_email')