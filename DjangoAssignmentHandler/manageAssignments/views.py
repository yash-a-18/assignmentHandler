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
        return render(request,'AssignmentPage.html')
    else:
        return HttpResponseRedirect('/')

def putAssignmentData(request):
    
    if request.user.is_authenticated:
        #t_assign_id=request.POST.get('assign_id',default=False)
        t_assign_name=request.POST.get('assign_name',default=None)
        t_teacher_email=request.POST.get('teacher_email',default=False)
        t_c_id=request.POST.get('c_id',default=None)
        t_initial_date=request.POST.get('initial_date',default=None)
        t_assign_due_date=request.POST.get('assign_due_date',default=None)
        t_assign_max_size_kb=request.POST.get('assign_max_size_kb',default=None)
        assign=Assignment(#assign_id=t_assign_id,
                        assign_name=t_assign_name,
                        teacher_email=t_teacher_email,
                        c_id=t_c_id,
                        initial_date=t_initial_date,
                        assign_due_date=t_assign_due_date,
                        assign_max_size_kb=t_assign_max_size_kb                  
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

    
def studentAssignmentDisplay(request):
    if request.user.is_authenticated:
        return render(request,'StudentAssignmentDisplay.html')
    else:
        return HttpResponseRedirect('/')


def teacherAssignmentDisplay(request):
    #list of assignments created by the logged in teacher
    if request.user.is_authenticated:
        ass_list=Assignment.objects.filter(teacher_email=request.user.username)
        ass_list.reverse()
        c={'ass_list':ass_list}
        c.update(csrf(request))
        return render(request,"TeacherAssignmentDisplay.html",c)
    else:
        return HttpResponseRedirect('/')
