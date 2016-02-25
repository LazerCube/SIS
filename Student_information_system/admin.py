from django.contrib import admin
from .models import tblStudent, tblUnits, tblClasses

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'date_of_birth' ,'gender' ,'id_foreign_classes')
    list_filter = ['gender']
    search_fields = ['name_first', 'name_last']


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_code', 'id_foreign_unit_1', 'id_foreign_unit_2',  'id_foreign_unit_3')
    fieldsets = [
        (None,          {'fields':['class_code']}),
        ('Units',          {'fields':   ['id_foreign_unit_1',
                                        'id_foreign_unit_2',
                                        'id_foreign_unit_3']}),
    ]

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name_unit','description')


admin.site.register(tblStudent, StudentAdmin)
admin.site.register(tblClasses, ClassAdmin)
admin.site.register(tblUnits, UnitAdmin)
