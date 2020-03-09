from django.urls import path

from . import views

urlpatterns=[
    path('SubmissionPage.html',views.submissionPage,name='submission_page')
    
]