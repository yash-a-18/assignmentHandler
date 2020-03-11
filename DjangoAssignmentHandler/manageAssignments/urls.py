from django.urls import path

from . import views

urlpatterns=[
    path('AssignmentPage.html',views.AssignmentPage,name='AssignmentPage'),
    path('createAssignment',views.putAssignmentData,name='putAssignmentData')
]