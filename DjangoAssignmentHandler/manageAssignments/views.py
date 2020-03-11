from django.shortcuts import render
from django.contrib import messages
from manageAssignments.models import Assignment
# Create your views here.
def AssignmentPage(request):
    return render(request,'AssignmentPage.html')
def putAssignmentData(request):
    t_assign_id=request.POST.get('assign_id',default=false)
    t_assign_name=request.POST.get('assign_name',default=none)
    t_teacher_email=request.POST.get('teacher_email',default=false)
    t_c_id=request.POST.get('c_id',default=none)
    t_initial_date=request.POST.get('initial_date',default=none)
    t_assign_due_date=request.POST.get('assign_due_date',default=none)
    t_assign_max_size_kb=request.POST.get('assign_max_size_kb',default=none)
    assign=Assignment(assign_id=t_assign_id,
                      assign_name=t_assign_name,
                      teacher_email=t_teacher_email,
                      c_id=t_c_id,
                      initial_date=t_initial_date,
                      assign_due_date=t_assign_due_date,
                      assign_max_size_kb=t_assign_max_size_kb                      
                    )
    assign.save()
    return render(request,'AssignmentPage.html',message.success(request,'Assignment added successfully!!!'))