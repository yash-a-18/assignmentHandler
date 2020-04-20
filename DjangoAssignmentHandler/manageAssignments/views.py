from django.shortcuts import render
from django.contrib import messages
from manageAssignments.models import Assignment
from manageSubmissions.models import Submission
from RegistrationModule.models import StudentCourse,Student,Courses
from django.template.context_processors import csrf
import datetime
from django.http import HttpResponseRedirect


# Create your views here.
def AssignmentPage(request):
    if request.user.is_authenticated:
        c={}
        c["teacher_email"]=request.user.username
        c["course_list"]=Courses.objects.all()
        c.update(csrf(request))
        return render(request,'AssignmentPage.html',c)
    else:
        return HttpResponseRedirect('/')

def putAssignmentData(request):
    
    if request.user.is_authenticated:
        #t_assign_id=request.POST.get('assign_id',default=False)
        t_assign_name=request.POST.get('assign_name',default=None)
        t_teacher_email=request.POST.get('teacher_email',default=False)
        t_c_id=request.POST.get('c_id',default=None)
        
        if request.POST.get('initial_date',default=None) ==None:
            t_initial_date=datetime.date.today()#auto init date
        else:
            t_initial_date=request.POST.get('initial_date',default=None)
        t_assign_due_date=request.POST.get('assign_due_date',default=None)
        t_assign_max_size_kb=request.POST.get('assignment_max_upload_size',default=1000)
        t_assign_file=request.FILES['assignment_file']
        assign=Assignment(#assign_id=t_assign_id,
                        assign_name=t_assign_name,
                        teacher_email=t_teacher_email,
                        c_id=t_c_id,
                        initial_date=t_initial_date,
                        assign_due_date=t_assign_due_date,
                        assign_max_size_kb=t_assign_max_size_kb,
                        assign_file=t_assign_file                  
                        )
        assign.save()
        return render(request,'AssignmentPage.html',messages.success(request,'Assignment added successfully!!!'))
    else:
        return HttpResponseRedirect('/')

# Create your views here.
def displayStudentAssignmentList(request):
    if request.user.is_authenticated:
        try:
            student_course=StudentCourse.objects.filter(student_email=request.user.username)
            student_submitted_ass=Submission.objects.filter(student_email=request.user.username)
            student_submitted_ass_id=[ass.assign_id for ass in student_submitted_ass]

            #ass_list=Assignment.objects.all()
            ass_list=[]
            for course in student_course:
                    all_assign=Assignment.objects.filter(c_id=course.c_id).filter(assign_due_date__gte=datetime.date.today())
                    for temp_ass in all_assign:
                        if temp_ass.assign_id not in student_submitted_ass_id:
                            ass_list.append(temp_ass)
                #print(ass_list[0].c_id)
        except Student.DoesNotExist:
            ass_list = None
        
        c={'ass_list':ass_list}
        c.update(csrf(request))
        return render(request,"StudentHomePage.html",c)
    else:
        return HttpResponseRedirect('/')

    

def teacherHomePage(request):
    if request.user.is_authenticated:
        c={}
        ass_list=Assignment.objects.filter(teacher_email=request.user.username)
        c['ass_list']=ass_list
        c.update(csrf(request))
        return render(request,'TeacherHomePage.html',c)
    else:
        return HttpResponseRedirect('/')
'''
def teacherAssignmentList(request):
    if request.user.is_authenticated:
        c={}
        
    else:
        return HttpResponseRedirect('/')
        '''