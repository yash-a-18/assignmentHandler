from django.shortcuts import render
import datetime
from django.db import models
from manageSubmissions.models import Assignment
from RegistrationModule.models import StudentCourse,Student,Courses
# Create your views here.
def submissionPage(request):
    student_data=Student.objects.get(student_email=request.user.username)
    student_course=StudentCourse.objects.get(student_email=student_data.student_email)
    '''28/02/2020'''
    #all_assign=Assignment.object.all()
    ass_id_list=[]
    todays_date=datetime.datetime()
    for course in student_course:
        #all_assign=Assignment.object.all(c_id=course.c_id)

        all_assign=Assignment.objects.filter(models.Q(c_id=course.c_id) & models.Q(assign_due_date>todays_date))
        ass_id_list.append(all_assign)
    print(ass_id_list)
    
    return render(request,'SubmissionPage.html')