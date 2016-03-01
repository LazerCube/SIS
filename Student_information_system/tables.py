import django_tables2 as tables
from .models import tblStudent, tblClasses, tblUnits

from django_tables2.utils import A

class StudentTable(tables.Table):
    name_first = tables.LinkColumn('SIS:students', args=[A('pk')])
    name_last = tables.LinkColumn('SIS:students', args=[A('pk')])
    date_of_birth = tables.DateColumn()
    gender = tables.BooleanColumn()
    travel_time = tables.Column()
    post_code = tables.Column()
    id_foreign_classes = tables.LinkColumn('SIS:classes', args=[A('id_foreign_classes.pk')])

    class Meta:
        template = 'django_tables/tables.html'
        attrs = {'class': 'table'}

class ClassTable(tables.Table):
    class_code = tables.LinkColumn('SIS:classes', args=[A('pk')])
    id_foreign_unit_1 = tables.LinkColumn('SIS:units', args=[A('id_foreign_unit_1.pk')])
    id_foreign_unit_2 = tables.LinkColumn('SIS:units', args=[A('id_foreign_unit_2.pk')])
    id_foreign_unit_3 = tables.LinkColumn('SIS:units', args=[A('id_foreign_unit_3.pk')])

    class Meta:
        template = 'django_tables/tables.html'
        attrs = {'class': 'table'}

class UnitsTable(tables.Table):
    name_unit = tables.LinkColumn('SIS:units', args=[A('pk')])
    description = tables.Column()

    class Meta:
        template = 'django_tables/tables.html'
        attrs = {'class': 'table'}
