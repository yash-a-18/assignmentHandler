from django.shortcuts import render
<<<<<<< HEAD
import cgi,os,sys
import cgitb
from django.contrib import messages
from manageAssignments.models import Assignment
# Create your views here.



def uploadFile(request):
    cgitb.enable()
    #Setting stdio set for binary modes in windows
    try:
        import msvcrt 
        msvcrt.setmode(0,os.O_BINARY) #for stdin=0
        msvcrt.setmode(1,os.O_BINARY) #for stdin=1
    except ImportError:
        pass
    form=cgi.FieldStorage()
    filename=form['student_file']

    #Checking whether the file was uploaded or not
    if filename.student_file:
        #Creates a new file on the web server of the same name and writes the data of the file to the newly created file on the server
        fn=os.path.basename(filename.student_file)
        open(fn,'wb').write(filename.file.read(250000))     #assuminng max file size to 250kb
        mssg="The file is uploaded successfully!!"
    else:
        mssg="No file uploaded"
    return render(request,'SubmissionPage.html',message.success(request,mssg))

#def downloadFile(request):
=======
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
>>>>>>> b84af62b03b2aaae0d544a8c092c0ab9fb711c34
