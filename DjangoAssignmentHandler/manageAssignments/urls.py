from django.urls import path

from . import views

urlpatterns=[
    path('StudentHomePage.html',views.displayStudentAssignmentList,name='student_home')

    
]
