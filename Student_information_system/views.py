from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import tblStudent, tblClasses, tblUnits

from django_tables2   import RequestConfig
from .tables  import StudentTable, ClassTable, UnitsTable

def index(request):
    return render(request, 'SIS/index.html')

def students(request, student_id):
    student = get_object_or_404(tblStudent, pk=student_id)
    context = {
        'student': student,
    }
    return render(request, 'SIS/studentView.html', context)

def classes(request, class_id):
    class_id = get_object_or_404(tblClasses, pk=class_id)
    context = {
        'class': class_id,
    }
    return render(request, 'SIS/classView.html', context)

def units(request, unit_id):
    units = get_object_or_404(tblUnits, pk=unit_id)
    context = {
        'unit': units,
    }
    return render(request, 'SIS/unitView.html', context)

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
