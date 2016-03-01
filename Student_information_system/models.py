from __future__ import unicode_literals
from django.db import models

class tblUnits(models.Model):
    id_units = models.AutoField(primary_key=True)
    name_unit = models.CharField("Unit Name", max_length=200)
    description = models.TextField("Description", max_length=300, null=True,
                                    blank=False, default="None")

    class Meta:
        verbose_name = ("Unit")
        verbose_name_plural = ("Units")

    def __str__(self):
        return self.name_unit

class tblClasses(models.Model):
    id_classes = models.AutoField(primary_key=True, verbose_name="Class ID")
    class_code = models.CharField("Class Code", max_length=50)
    id_foreign_unit_1 = models.ForeignKey(tblUnits, on_delete=models.CASCADE,
                                        verbose_name="Unit 1", related_name='Unit_1',
                                        null=True, blank=True)
    id_foreign_unit_2 = models.ForeignKey(tblUnits, on_delete=models.CASCADE,
                                        verbose_name="Unit 2", related_name='Unit_2',
                                        null=True, blank=True)
    id_foreign_unit_3 = models.ForeignKey(tblUnits, on_delete=models.CASCADE,
                                        verbose_name="Unit 3", related_name='Unit_3',
                                        null=True, blank=True)

    class Meta:
        verbose_name = ("Class")
        verbose_name_plural = ("Classes")

    def __str__(self):
        return self.class_code

class tblStudent(models.Model):
    id_students = models.AutoField(primary_key=True, verbose_name="Student ID")
    name_first = models.CharField("First Name", max_length=200)
    name_last = models.CharField("Last Name", max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.NullBooleanField("Is Male", null=True, blank=True)
    travel_time = models.DurationField("Travel Time", null=True, blank=True)
    post_code = models.CharField("Post Code", max_length=7, null=True, blank=True)
    id_foreign_classes = models.ForeignKey(tblClasses, on_delete=models.CASCADE, verbose_name="Class")


    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")


    def __str__(self):
        return ("%s %s | %s" %(self.name_first, self.name_last, self.id_foreign_classes))
