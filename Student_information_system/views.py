from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import tblStudent, tblClasses, tblUnits

from django_tables2   import RequestConfig
from .tables  import StudentTable, ClassTable, UnitsTable

def index(request):
    return HttpResponse('Index')

def students(request, student_id):
    student = get_object_or_404(tblStudent, pk=student_id)
    context = {
        'student': student,
    }
    return render(request, 'SIS/index.html', context)

def studentsOverview(request):
    title = "Students"
    table = StudentTable(tblStudent.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    context = {
        'table': table,
        'page_title': title,
    }

    return render(request, 'SIS/tableViews.html', context)

def classesOverview(request):
    title = "Classes"
    table = ClassTable(tblClasses.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(table)

    context = {
        'table': table,
        'page_title': title,
    }

    return render(request, 'SIS/tableViews.html', context)

def unitsOverview(request):
    title = "Units"
    table = UnitsTable(tblUnits.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(table)

    context = {
        'table': table,
        'page_title': title,
    }

    return render(request, 'SIS/tableViews.html', context)
