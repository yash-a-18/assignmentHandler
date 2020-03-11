from django.shortcuts import render
import cgi,os,sys
import cgitb
from django.contrib import messages
from manageAssignments.models import Assignment
# Create your views here.



def uploadFile(request):
    cgitb.enable()
    #Setting stdio set for binary modes in windows
    try:
        import msvcrt 
        msvcrt.setmode(0,os.O_BINARY) #for stdin=0
        msvcrt.setmode(1,os.O_BINARY) #for stdin=1
    except ImportError:
        pass
    form=cgi.FieldStorage()
    filename=form['student_file']

    #Checking whether the file was uploaded or not
    if filename.student_file:
        #Creates a new file on the web server of the same name and writes the data of the file to the newly created file on the server
        fn=os.path.basename(filename.student_file)
        open(fn,'wb').write(filename.file.read(250000))     #assuminng max file size to 250kb
        mssg="The file is uploaded successfully!!"
    else:
        mssg="No file uploaded"
    return render(request,'SubmissionPage.html',message.success(request,mssg))

#def downloadFile(request):
