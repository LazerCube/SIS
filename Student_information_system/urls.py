from django.conf.urls import url
from . import views

app_name= 'SIS'
urlpatterns=[
    url(r'^student/$', views.students, name='students'),
]
