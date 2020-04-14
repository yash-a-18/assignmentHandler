from django.shortcuts import render
#<<<<<<< HEAD
import cgi,os,sys
import cgitb
from django.contrib import messages
from manageAssignments.models import Assignment
import datetime
from django.db import models
from django.http import HttpResponseRedirect
from RegistrationModule.models import StudentCourse,Student,Courses
from django.template.context_processors import csrf
from manageSubmissions.models import Submission
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required

'''def uploadFile(request):
    if request.user.is_authenticated:
        cgitb.enable()
        #Setting stdio set for binary modes in windows
        try:
            import msvcrt 
            msvcrt.setmode(0,os.O_BINARY) #for stdin=0
            msvcrt.setmode(1,os.O_BINARY) #for stdin=1
        except ImportError:
            pass
        form=cgi.FieldStorage()
        print(form)
        filename=form['student_file']

        #Checking whether the file was uploaded or not
        if filename.student_file:
            #Creates a new file on the web server of the same name and writes the data of the file to the newly created file on the server
            fn=os.path.basename(filename.student_file)
            open(fn,'wb').write(filename.file.read(250000))     #assuminng max file size to 250kb
            mssg="The file is uploaded successfully!!"
        else:
            mssg="No file uploaded"
        return render(request,'SubmissionPage.html',messages.success(request,mssg))
    else:
        return HttpResponseRedirect('/',{'message':'Please Login'})

#def downloadFile(request):
#=======
'''

def addSubmission(request):
    if request.user.is_authenticated:
        if True:
            #Creates a new file on the web server of the same name and writes the data of the file to the newly created file on the server
            '''
            fn=os.path.basename(filename.student_file)
            open(fn,'wb').write(filename.file.read(250000))     #assuminng max file size to 250kb
            '''
            t_assign_id=request.POST.get('student_assignment_id')
            t_student_email=request.POST.get('student_submission_email')
            t_submission_date=datetime.datetime.now()
            t_submission_file_name=request.FILES['student_file']
            sub=Submission(assign_id=t_assign_id,student_email=t_student_email,submission_date=t_submission_date,submission_file_name=t_submission_file_name)
            sub.save()
            mssg="The file is uploaded successfully!!"
        else:
            mssg="No file uploaded"
        return render(request,'SubmissionPage.html',messages.success(request,mssg))
    else:
        return HttpResponseRedirect('/',{'message':'Please Login'})    

# Create your views here.
#@login_required(login_url='')
def submissionPage(request):
    #print(request.user.username)
    if request.user.is_authenticated:
        try:
            student_course=StudentCourse.objects.filter(student_email=request.user.username)
            student_submitted_ass=Submission.objects.filter(student_email=request.user.username)
            student_submitted_ass_id=[ass.assign_id for ass in student_submitted_ass]

            #print(student_course[0].c_id)
            #print(StudentCourse.objects.all()[0].student_email)
            '''28/02/2020'''
            #all_assign=Assignment.object.all()
            ass_id_list=[]
            home_ass_id=None
            if request.GET.get('assign_id'):
                home_ass_id=int(request.GET.get('assign_id'))
                
            for course in student_course:
                all_assign=Assignment.objects.filter(c_id=course.c_id).filter(assign_due_date__gte=datetime.date.today())
                for temp_ass in all_assign:
                    if temp_ass.assign_id not in student_submitted_ass_id:
                        ass_id_list.append(temp_ass)
            #print(ass_id_list[0].c_id)
        except Student.DoesNotExist:
            ass_id_list = None
        c={'ass_list':ass_id_list,'student_email':request.user.username,'ass_id':home_ass_id}
        c.update(csrf(request))
        return render(request,'SubmissionPage.html',c)
    else:
        return HttpResponseRedirect('/',{'message':'Please Login'})
'''
def addSubmission(request):
    #logic to add submission file on system and
    pass
>>>>>>> b84af62b03b2aaae0d544a8c092c0ab9fb711c34
'''
def studentSubmissionDisplay(request):
    if request.user.is_authenticated:
        c={}
        #teacher_email=request.user.username
        course_list=StudentCourse.objects.filter(student_email=request.user.username)
        c['course_list']=course_list
        
        if request.method =="POST" and request.POST.get("student_course_name")!="Choose...":
            c['course_option']=request.POST.get("student_course_name")

            t_course_id=request.POST.get("student_course_id")
            #c['course_option']=t_course_id
            sub_list=Submission.objects.filter(student_email=request.user.username)#.filter(c_id=t_course_id)
            updated_sub_list=[]
            for sub in sub_list:
                if sub.submission_marks_uniqueness!=None:
                    updated_sub_list.append(sub)
            #c['sub_list']=updated_sub_list
            c['sub_list']=sub_list
            
        c.update(csrf(request))
        return render(request,'StudentSubmissionDisplay.html',c)
    else:
        return HttpResponseRedirect('/')

#@xframe_options_exempt
def viewSubmissionFile(request):
    if request.user.is_authenticated:
        c={}
        try:
            t_stu_email=request.GET.get("stu_email")
            t_assign_id=request.GET.get("assign_id")
            
            file_url=Submission.objects.get(student_email=t_stu_email,assign_id=t_assign_id).submission_file_name.url
            #c['file_url']=file_url
            file_name=file_url.split('/')
            file_name.reverse()
            c['file_name']=file_name[0]
            f = open(os.path.dirname(__file__)+'\\..\\media\\'+file_name[1]+'\\'+file_name[0], 'r')
            
            c['file_content']=f.read()
            c['stu_email']=t_stu_email
            c['assign_id']=t_assign_id
        except Submission.DoesNotExist:
            print("MyError: At manageSubmissioin.views.viewSubmissionFile() try block ")
        c.update(csrf(request))
        return render(request,'ViewSubmissionFile.html',c)

    else:
        return HttpResponseRedirect('/')


def teacherSubmissionDisplay(request):
    #list of assignments created by the logged in teacher
    if request.user.is_authenticated:
        c={}
        #teacher_email=request.user.username
        course_list=Courses.objects.all()
        c['course_list']=course_list
        if request.method =="POST" and request.POST.get("teacher_course_name")!="Choose...":
            #c['course_option']=request.POST.get("teacher_course_name")

            t_course_id=request.POST.get("teacher_course_id")
            c['course_option']=t_course_id
            #print(t_course_id)
            #print(request.user.username)
            ass_list=Assignment.objects.filter(c_id=t_course_id).filter(teacher_email=request.user.username)
            c['ass_list']=ass_list
            
            if request.POST.get("teacher_assignment_id") != None and request.POST.get("teacher_assignment_id")!="Choose...":
                #print(request.POST.get("teacher_assignment_id"))
                c['assign_option']=int(request.POST.get("teacher_assignment_id")) ##beware of the data types
                '''print("{}=={}".format(type(ass_list[0].assign_id),type(request.POST.get("teacher_assignment_id"))))'''
                sub_list=Submission.objects.filter(assign_id=int(request.POST.get("teacher_assignment_id")))
                #sub_list.reverse()
                sub_list_unmarked=[]
                for sub in sub_list:
                    if(sub.submission_marks_logic==None):
                        sub_list_unmarked.append(sub)
                c['sub_list_unmarked']=sub_list_unmarked

        c.update(csrf(request))
        return render(request,"TeacherSubmissionDisplay.html",c)            
    else:
        return HttpResponseRedirect('/')


def setSubmissionMarks(request):
    
    t_stu_email=request.POST.get('student_email')
    t_assign_id=request.POST.get('assign_id')
    t_mk_l=request.POST.get('submission_marks_logic')
    t_mk_u=request.POST.get('submission_marks_uniqueness')
    t_mk_q=request.POST.get('submission_marks_quality')
    try:
        sub=Submission.objects.get(student_email=t_stu_email,assign_id=t_assign_id)
        sub.submission_marks_logic=t_mk_l
        sub.submission_marks_uniqueness=t_mk_u
        sub.submission_marks_quality=t_mk_q
        sub.save()
    except Submission.DoesNotExist:
        print('Error at manageSubmission.setSubmission():submission not found')
        print(t_assign_id)
        print(t_stu_email)
        
    return HttpResponseRedirect("TeacherSubmissionDisplay.html")