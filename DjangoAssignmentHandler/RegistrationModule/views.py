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
