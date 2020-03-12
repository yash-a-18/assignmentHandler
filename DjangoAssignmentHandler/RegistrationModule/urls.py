from django.urls import path

from . import views

urlpatterns=[
    path('sign_in.html',views.signInUser,name='sign_in'),
    path('teacher_reg.html',views.teacherReg,name='teacher_reg'),
    path('student_reg.html',views.studentReg,name='student_reg'),
<<<<<<< HEAD
    path('login(test).html',views.login,name='login'),
]
=======
    path('Login.html',views.login,name='login'),
    path('authentication.html',views.authentication,name='authentication'),
    path('putStudentData',views.putStudentData,name='putStudentData'),
    path('putTeacherData',views.putTeacherData,name='putTeacherData'),
]
>>>>>>> b84af62b03b2aaae0d544a8c092c0ab9fb711c34
