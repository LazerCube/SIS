from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

def students(request):
    return HttpResponse('Student!')
