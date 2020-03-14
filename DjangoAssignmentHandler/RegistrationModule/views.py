from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import include,path
from django.contrib import auth  
from django.template.context_processors import csrf  
from django.views.generic import TemplateView 
from django.contrib.auth.models import User
from django.contrib import messages
from RegistrationModule.models import Teacher, Student
from django.core.files.storage import FileSystemStorage
# Create your views here.
def signInUser(request):
    return render(request,'sign_in.html')

def teacherReg(request):
    return render(request, 'teacher_reg.html')

def studentReg(request):
    return render(request, 'student_reg.html')

def login(request):
    
    message='Well done!'
    c={'message':message}
    c.update(csrf(request))

    #return render(request,'login(test).html',c,messages.success(request,'Hello User'))
    return render(request,'Login.html',c)


def logout(request):
    
    if request.user.is_authenticated:
        auth.logout(request)
        message='Successfully logged out!'
        c={'message':message}
        c.update(csrf(request))

        #return render(request,'login(test).html',c,messages.success(request,'Hello User'))
        return render(request,'Login.html',c)
    else:
        return HttpResponseRedirect('/')

def putStudentData(request):
    
    t_first_name=request.POST.get('student_first_name',default=None)
    t_middle_name=request.POST.get('student_middle_name',default=None)
    t_last_name=request.POST.get('student_last_name',default=None)
    t_username=request.POST.get('student_user_name',default=None)
    t_password=request.POST.get('student_password',default=None)
    t_dob=request.POST.get('student_dob',default=None)
    t_semester=request.POST.get('student_semester',default=None)
    t_course=request.POST.get('student_course',default=None)
    t_stu_email=request.POST.get('student_email',default=None)
    t_address=request.POST.get('student_address',default=None)
    t_address2=request.POST.get('student_address2',default=None)
    t_city=request.POST.get('student_city',default=None)
    t_state=request.POST.get('student_state',default=None)
    t_zip_code=request.POST.get('student_zip',default=None)
    t_mobile_no=request.POST.get('student_mobile_no',default=None)
    t_id_no=request.POST.get('student_id_no',default=None)
    #t_image=request.FILES('student_image',default=None)
    stu=Student(student_first_name=t_first_name,
                student_middle_name=t_middle_name,
                student_last_name=t_last_name,
                student_username=t_username,
                student_dob=t_dob,
                student_semester=t_semester,
                #student_course=t_course,
                student_email=t_stu_email,
                student_address=t_address,
                student_address2=t_address2,
                student_city=t_city,
                student_state=t_state,
                student_zip=t_zip_code,
                student_mobile_no=t_mobile_no,
                student_id_no=t_id_no,
    #            student_image=t_image
                )
    stu.save()
    user=User(username=t_stu_email,password=t_password )
    user.save()
    

    message="Hey there Student!! , you are now successfully registered"
    c={'message':message}
    c.update(csrf(request))
    return render(request ,'Login.html',c)
#<<<<<<< HEAD
    #return render(request,'login(test).html')
    def uploadStudentImage(request):
        if request.method=='POST':
            t_image=request.FILES('student_image')
            fs=FileSystemStorage()
            name=fs.save(t_image.name,t_image)



'''def putTeacherData(request):
    
    t_first_name=request.POST.get('teacher_first_name',default=None)
    t_middle_name=request.POST.get('teacher_middle_name',default=None)
    t_last_name=request.POST.get('teacher_last_name',default=None)
    t_username=request.POST.get('user_name',default=None)
    t_password=request.POST.get('teacher_password',default=None)
    t_dob=request.POST.get('teacher_dob',default=None)
    t_semester=request.POST.get('teacher_semester',default=None)
    t_course=request.POST.get('teacher_course',default=None)
    t_tchr_email=request.POST.get('teacher_email',default=None)
    t_address=request.POST.get('teacher_address',default=None)
    t_address2=request.POST.get('teacher_address2',default=None)
    t_city=request.POST.get('teacher_city',default=None)
    t_state=request.POST.get('teacher_state',default=None)
    t_zip_code=request.POST.get('teacher_zip',default=None)
    t_mobile_no=request.POST.get('teacher_mobile_no',default=None)
    t_id_no=request.POST.get('teacher_id_no',default=None)
    t_image=request.FILES('teacher_image',default=None)
#=======
    message="Hey there Student!! , you are now successfully registered"
    c={'message':message}
    c.update(csrf(request))
    return render(request ,'Login.html',c)
    #return HttpResponseRedirect('Login.html',c)
'''
def putTeacherData(request):
    t_first_name=request.POST.get('teacher_first_name',default=None)
    t_middle_name=request.POST.get('teacher_middle_name',default=None)
    t_last_name=request.POST.get('teacher_last_name',default=None)
    t_username=request.POST.get('user_name',default=None)
    t_password=request.POST.get('teacher_password',default=None)
    t_dob=request.POST.get('teacher_dob',default=None)
    t_semester=request.POST.get('teacher_semester',default=None)
    t_course=request.POST.get('teacher_course',default=None)
    t_tchr_email=request.POST.get('teacher_email',default=None)
    t_address=request.POST.get('teacher_address',default=None)
    t_address2=request.POST.get('teacher_address2',default=None)
    t_city=request.POST.get('teacher_city',default=None)
    t_state=request.POST.get('teacher_state',default=None)
    t_zip_code=request.POST.get('teacher_zip',default=None)
    t_mobile_no=request.POST.get('teacher_mobile_no',default=None)
    t_id_no=request.POST.get('teacher_id_no',default=None)
    t_image=request.FILES('teacher_image',default=None)
    tchr=Teacher(first_name=t_first_name,
                middle_name=t_middle_name,
                last_name=t_last_name,
                username=t_username,
                dob=t_dob,
                semester=t_semester,
                course=t_course,
                teacher_email=t_tchr_email,
                address=t_address,
                address2=t_address2,
                city=t_city,
                state=t_state,
                zip_code=t_zip_code,
                mobile_no=t_mobile_no,
                id_no=t_id_no,
                image=t_image)
    tchr.save()
    user=User(username=t_tchr_email,password=t_password )
    user.save()
    message="Hey there Teacher!! , you are now successfully registered"
    c={'message':message}
    c.update(csrf(request))
    
    return render(request ,'Login.html',c)
    #return HttpResponseRedirect('Login.html',c)

def authentication(request):
    username=request.POST.get('user_name',default=None)
    password=request.POST.get('user_password',default=None)
    User=auth.authenticate(username=username,password=password)
    print(User)
    if User is not None:
        auth.login(request,User)
        #return HttpResponseRedirect(request,'/manageAssignment/StudentHomePage.html')
        return HttpResponseRedirect('/manageAssignments/StudentHomePage.html')
    else:
        #messages.error(request, 'Invalid Username/Password..')
        message='Invalid Username/Password..'
        c={'message':message}
        c.update(csrf(request))
        return render(request,'Login.html',c)