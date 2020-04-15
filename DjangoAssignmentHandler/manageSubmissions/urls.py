from django.urls import path

from . import views

urlpatterns=[
    path('SubmissionPage.html',views.submissionPage,name='submission_page'),
    path('addSubmission',views.addSubmission,name='addSubmission'),
    path('SetSubmissionMarks',views.setSubmissionMarks,name='setSubmissionMarks'),
    path('StudentSubmissionDisplay.html',views.studentSubmissionDisplay,name='StudentSubmissionDisplay'),
    path('ViewSubmissionFile.html',views.viewSubmissionFile,name='view_submission_file'),
    path('TeacherSubmissionDisplay.html',views.teacherSubmissionDisplay,name='TeacherAssignmentDisplay'),
]