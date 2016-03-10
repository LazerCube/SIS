from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponseRedirect(reverse('SIS:index'))

def page_not_found(request):
    context = {
        'error_code': 404,
    }
    return render(request, 'error.html', context)

def server_error(request):
    context = {
        'error_code': 500,
    }
    return render(request, 'error.html', context)
