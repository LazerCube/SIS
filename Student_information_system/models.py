from __future__ import unicode_literals
from django.db import models

class tblUnits(models.Model):
    id_units = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300)

class tblClasses(models.Model):
    id_classes = models.AutoField(primary_key=True)
    class_code = models.CharField(max_length=50)
    id_foreign_units = models.ForeignKey(tblUnits, on_delete=models.CASCADE)

class tblStudent(models.Model):
    id_students = models.AutoField(primary_key=True)
    name_first = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    gender = models.BooleanField()
    id_foreign_classes = models.ForeignKey(tblClasses, on_delete=models.CASCADE)
