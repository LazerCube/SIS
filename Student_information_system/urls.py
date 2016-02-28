from django.conf.urls import url
from . import views

app_name= 'SIS'
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^students/$', views.studentsOverview, name='studentsOverview'),
    url(r'^students/(?P<student_id>[0-9]+)/overview$', views.students, name='students'),
    url(r'^classes/$', views.classesOverview, name='classesOverview'),
    url(r'^classes/(?P<class_id>[0-9]+)/overview$', views.classes, name='classes'),
    url(r'^units/$', views.unitsOverview, name='unitsOverview'),
    url(r'^units/(?P<unit_id>[0-9]+)/overview$', views.units, name='units'),
]
