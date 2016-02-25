from django.conf.urls import url
from . import views

app_name= 'SIS'
urlpatterns=[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^student/(?P<pk>[0-9]+)$', views.StudentView.as_view(), name='students'),
    url(r'^class/$', views.classes, name='classes'),
    url(r'^unit/$', views.units, name='units'),
]
