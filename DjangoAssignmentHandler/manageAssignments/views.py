from django.shortcuts import render

# Create your views here.
def displayStudentAssignmentList(request):
    ass_list=Assignment.object.getAll()
    return render(request,"StudentHomePage.html",{"ass_list":ass_list})
