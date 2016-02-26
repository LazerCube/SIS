from django.conf.urls import url
from . import views

app_name= 'SIS'
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^student/$', views.studentsOverview, name='studentsOverview'),
    url(r'^student/(?P<student_id>[0-9]+)/overview$', views.students, name='students'),
    url(r'^classes/$', views.classesOverview, name='classesOverview'),
    url(r'^units/$', views.unitsOverview, name='unitsOverview'),
]
