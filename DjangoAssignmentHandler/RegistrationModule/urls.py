from django.urls import path

from . import views

urlpatterns=[
    path('sign_in.html',views.signInUser,name='sign_in'),
    path('teacher_reg.html',views.teacherReg,name='teacher_reg'),
    path('student_reg.html',views.studentReg,name='student_reg'),
    
]