from __future__ import unicode_literals
from django.db import models

class tblUnits(models.Model):
    id_units = models.AutoField(primary_key=True)
    name_unit = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name_unit

class tblClasses(models.Model):
    id_classes = models.AutoField(primary_key=True)
    class_code = models.CharField(max_length=50)
    id_foreign_units = models.ForeignKey(tblUnits, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_code

class tblStudent(models.Model):
    id_students = models.AutoField(primary_key=True)
    name_first = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.BooleanField()
    id_foreign_classes = models.ForeignKey(tblClasses, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s %s | %s" %(self.name_first, self.name_last, self.id_foreign_classes))
