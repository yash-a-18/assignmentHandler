from django.shortcuts import render
from django.http import HttpResponse
from django.urls import include,path
# Create your views here.
def signInUser(request):
    return render(request,'sign_in.html')

def teacherReg(request):
    return render(request, 'teacher_reg.html')

def studentReg(request):
    return render(request, 'student_reg.html')

def putStudentData(request):
    t_first_name=request.POST.get('student_first_name',default=none)
    t_middle_name=request.POST.get('student_middle_name',default=none)
    t_last_name=request.POST.get('student_last_name',default=none)
    t_username=request.POST.get('user_name',default=none)
    t_dob=request.POST.get('student_dob',default=none)
    t_semester=request.POST.get('student_semester',default=none)
    t_course=request.POST.get('student_course',default=none)
    t_stu_email=request.POST.get('student_email',default=none)
    t_address=request.POST.get('student_address',default=none)
    t_address2=request.POST.get('student_address2',default=none)
    t_city=request.POST.get('student_city',default=none)
    t_state=request.POST.get('student_state',default=none)
    t_zip_code=request.POST.get('student_zip',default=none)
    t_mobile_no=request.POST.get('student_mobile_no',default=none)
    t_id_no=request.POST.get('student_id_no',default=none)
    t_image=request.POST.get('student_image',default=none)
    stu=Student(first_name=t_first_name,
                middle_name=t_middle_name,
                last_name=t_last_name,
                username=t_username,
                dob=t_dob,
                semester=t_semester,
                course=t_course,
                stu_email=t_stu_email,
                address=t_address,
                address2=t_address2,
                city=t_city,
                state=t_state,
                zip_code=t_zip_code,
                mobile_no=t_mobile_no,
                id_no=t_id_no,
                image=t_image)
    stu.save()
    return HttpResponseRedirect(request,'sign_in.html')

def putTeacherData(request):
    t_first_name=request.POST.get('teacher_first_name',default=none)
    t_middle_name=request.POST.get('teacher_middle_name',default=none)
    t_last_name=request.POST.get('teacher_last_name',default=none)
    t_username=request.POST.get('user_name',default=none)
    t_dob=request.POST.get('teacher_dob',default=none)
    t_semester=request.POST.get('teacher_semester',default=none)
    t_course=request.POST.get('teacher_course',default=none)
    t_stu_email=request.POST.get('teacher_email',default=none)
    t_address=request.POST.get('teacher_address',default=none)
    t_address2=request.POST.get('teacher_address2',default=none)
    t_city=request.POST.get('teacher_city',default=none)
    t_state=request.POST.get('teacher_state',default=none)
    t_zip_code=request.POST.get('teacher_zip',default=none)
    t_mobile_no=request.POST.get('teacher_mobile_no',default=none)
    t_id_no=request.POST.get('teacher_id_no',default=none)
    t_image=request.POST.get('teacher_image',default=none)
    tchr=Teacher(first_name=t_first_name,
                middle_name=t_middle_name,
                last_name=t_last_name,
                username=t_username,
                dob=t_dob,
                semester=t_semester,
                course=t_course,
                stu_email=t_stu_email,
                address=t_address,
                address2=t_address2,
                city=t_city,
                state=t_state,
                zip_code=t_zip_code,
                mobile_no=t_mobile_no,
                id_no=t_id_no,
                image=t_image)
    tchr.save()
    return HttpResponseRedirect(request,'sign_in.html')