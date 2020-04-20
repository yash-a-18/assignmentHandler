from django.urls import path

from . import views

urlpatterns=[
    path('sign_in.html',views.signInUser,name='sign_in'),
    path('teacher_reg.html',views.teacherReg,name='teacher_reg'),
    path('student_reg.html',views.studentReg,name='student_reg'),
    path('StudentProfile.html',views.studentProfile,name='studentProfile'),
    path('TeacherProfile.html',views.teacherProfile,name='teacherProfile'),
    path('AddTeacherCourse',views.addTeacherCourse,name='addTeacherCourse'),
    path('RemoveTeacherCourse',views.removeTeacherCourse,name='removeTeacherCourse'),
    path('TeacherCourseDisplay.html',views.teacherCourseDisplay,name='teacherCourseDisplay'),
    path('Login.html',views.login,name='login'),
    path('',views.login,name='login'),
    path('authentication.html',views.authentication,name='authentication'),
    path('putStudentData',views.putStudentData,name='putStudentData'),
    path('putTeacherData',views.putTeacherData,name='putTeacherData'),
    path('Logout.html',views.logout,name='logout'),
    
]