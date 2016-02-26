import django_tables2 as tables
from .models import tblStudent, tblClasses, tblUnits

from django_tables2.utils import A

class StudentTable(tables.Table):
    name_first = tables.LinkColumn('SIS:students', args=[A('pk')])
    name_last = tables.LinkColumn('SIS:students', args=[A('pk')])
    date_of_birth = tables.DateColumn()
    gender = tables.BooleanColumn()
    id_foreign_classes = tables.Column()

    class Meta:
        template = 'django_tables/tables.html'
        attrs = {'class': 'table'}

class ClassTable(tables.Table):
    class_code = tables.Column()
    id_foreign_unit_1 = tables.Column()
    id_foreign_unit_2 = tables.Column()
    id_foreign_unit_3 = tables.Column()

    class Meta:
        template = 'django_tables/tables.html'
        attrs = {'class': 'table'}

class UnitsTable(tables.Table):
    name_unit = tables.Column()
    description = tables.Column()

    class Meta:
        template = 'django_tables/tables.html'
        attrs = {'class': 'table'}
