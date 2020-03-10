from django.shortcuts import render
import datetime
from django.db import models
from manageSubmissions.models import Assignment
from RegistrationModule.models import StudentCourse,Student,Courses
from django.template.context_processors import csrf


# Create your views here.
def submissionPage(request):
    #print(request.user.username)
    try:
        student_course=StudentCourse.objects.filter(student_email=request.user.username)
        #print(student_course[0].c_id)
        #print(StudentCourse.objects.all()[0].student_email)
        '''28/02/2020'''
        #all_assign=Assignment.object.all()
        ass_id_list=[]
        for course in student_course:
            all_assign=Assignment.objects.filter(c_id=course.c_id).filter(assign_due_date__gte=datetime.date.today())
            for temp_ass in all_assign:
                ass_id_list.append(temp_ass)
        #print(ass_id_list[0].c_id)
    except Student.DoesNotExist:
        ass_id_list = None
    c={'ass_list':ass_id_list}
    c.update(csrf(request))
    return render(request,'SubmissionPage.html',c)

def addSubmission(request):
    '''logic to add submission file on system and'''
    pass