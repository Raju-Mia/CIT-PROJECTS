
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from student.models import Student
# Create your views here.


def index(request):
    return HttpResponse("this is a student pages")

#this login required means --must should login.
from django.contrib.auth.decorators import login_required
@login_required
def all_student(request):
    
    try:
        all_date = Student.objects.filter(f_name = 'RAJON')
        # all_name_for_filter = Student.objects.filter(f_name__startswith = "r")
        # terget_data = Student.objects.get(f_name = "RAJON") # for GET value loop will be not working . called the value with the variable name.filde_names by templates file.
        
        # context = {'all_name_date': all_name_for_filter}
        context = {'all_data_name': all_date}

        # contexts = {'value':context, 'value2':context2}
        return render(request, "all_student.html", context)

    except Exception as e:
        mesg = "can't file the query all object by Student table"
        context = {'mesge': e}
        return render(request, "all_student.html", context)


from teacher.forms import TeacherForm
def create_student(request):
    if request.method == 'POST':
        form_value = TeacherForm(request.POST)
        if form_value.is_valid():
            form_value.save()

            return HttpResponse("your data succesfully submited") #this for cmd check

    form = TeacherForm()
    context = {'form': form}
    return render(request, 'create_student.html', context)
