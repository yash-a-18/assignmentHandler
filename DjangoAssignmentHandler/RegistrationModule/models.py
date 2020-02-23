from django.db import models

# Create your models here.##      &"C:\Program Files\sqlite\sqlite3.exe" .\db.sqlite3      ##to check changes


class Courses(models.Model):
    c_id=models.CharField(max_length=10,primary_key=True)
    c_name=models.CharField(max_length=20)
    c_credit=models.DecimalField(decimal_places=2,max_digits=5)

class Users(models.Model):
    user_email=models.CharField(max_length=50,primary_key=True)
    student_password=models.CharField(max_length=20)

class Student(models.Model):
    '''class for student db'''
    student_first_name=models.CharField(max_length=20)
    student_middle_name=models.CharField(max_length=20)
    student_last_name=models.CharField(max_length=20)
    student_username=models.CharField(max_length=100)
    #student_password=models.CharField(max_length=20) ##promoted to new users table
    student_dob=models.DateTimeField('date published')
    student_semester=models.IntegerField()
    #course=models.CharField(max_length=10) ##promoted to StudentCourse table
    student_email=models.CharField(max_length=50,primary_key=True)
    student_address=models.CharField(max_length=200)
    student_address2=models.CharField(max_length=200,default="NO_ADDR")
    student_city=models.CharField(max_length=20)
    student_state=models.CharField(max_length=20)
    student_zip=models.CharField(max_length=7)
    student_mobile_no=models.CharField(max_length=15)
    student_id_no=models.CharField(max_length=15)
    student_image=models.ImageField(upload_to='stu_pics')
    models.DateTimeField()

class StdentCourse(models.Model):
    student_email=models.CharField(max_length=50)
    c_id=models.CharField(max_length=10)
    models.ForeignKey(Courses,on_delete=models.CASCADE)
    models.ForeignKey(Student,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('student_email', 'c_id')

class Teacher(models.Model):
    '''db table for teachers'''
    teacher_first_name=models.CharField(max_length=20)
    teacher_middle_name=models.CharField(max_length=20)
    teacher_last_name=models.CharField(max_length=20)
    teacher_username=models.CharField(max_length=100)
    #teacher_password=models.CharField(max_length=20) ##promoted to new users table
    teacher_dob=models.DateTimeField('date published')
    #course=models.CharField(max_length=10)
    teacher_email=models.CharField(max_length=50,primary_key=True)
    teacher_address=models.CharField(max_length=200)
    teacher_address2=models.CharField(max_length=200,default="NO_ADDR")
    teacher_city=models.CharField(max_length=20)
    teacher_state=models.CharField(max_length=20)
    teacher_zip=models.CharField(max_length=7)
    teacher_mobile_no=models.CharField(max_length=15)
    teacher_id_no=models.CharField(max_length=15)
    teacher_image=models.ImageField(upload_to='teacher_pics')
    models.DateTimeField()


class Assignment(models.Model):
    assign_id=models.CharField(max_length=10,primary_key=True)
    assign_name=models.CharField(max_length=50)
    teacher_email=models.CharField(max_length=50)
    c_id=models.CharField(max_length=10)
    initial_date=models.DateTimeField()
    assign_due_date=models.DateTimeField()
    assign_max_size_kb=models.IntegerField()
    models.ForeignKey(Courses,on_delete=models.CASCADE)
    models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Submission(models.Model):
    assign_id=models.CharField(max_length=10)
    student_email=models.CharField(max_length=50)
    submission_date=models.DateTimeField()
    submission_file_name=models.CharField(max_length=50)
    submission_marks_logic=models.BooleanField(max_length=6)
    submission_marks_uniqueness=models.BooleanField(max_length=6)
    submission_marks_quality=models.BooleanField(max_length=6)
    models.ForeignKey(Assignment,on_delete=models.CASCADE)
    models.ForeignKey(Student,on_delete=models.CASCADE)
    '''to set a composite primary key'''
    class Meta:
        unique_together = ('assign_id', 'student_email')