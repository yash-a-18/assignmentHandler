from django.urls import path

from . import views

urlpatterns=[
#<<<<<<< HEAD
    path('AssignmentPage.html',views.AssignmentPage,name='AssignmentPage'),
    path('createAssignment',views.putAssignmentData,name='putAssignmentData'),
    path('StudentHomePage.html',views.displayStudentAssignmentList,name='student_home'),
    #path('StudentAssignmentDisplay.html',views.studentAssignmentDisplay,name='StudentAssignmentDisplay'),
    path('TeacherAssignmentDisplay.html',views.teacherAssignmentDisplay,name='TeacherAssignmentDisplay')
]
#>>>>>>> b84af62b03b2aaae0d544a8c092c0ab9fb711c34
