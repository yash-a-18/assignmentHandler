from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView

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
    path('password_reset/',PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
	path('password_reset/complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
	path('password_reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
	path('password_reset/done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    # path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    # path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('Logout.html',views.logout,name='logout'),
    
]