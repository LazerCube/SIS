from django.conf.urls import url
from . import views

app_name= 'SIS'
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^student/(?P<student_id>[0-9]+)/overview$', views.students, name='students'),
    url(r'^class/$', views.classes, name='classes'),
    url(r'^unit/$', views.units, name='units'),
]
