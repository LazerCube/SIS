from django.contrib import admin
from .models import tblStudent, tblUnits, tblClasses

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'date_of_birth' ,'gender' ,'id_foreign_classes')
    list_filter = ['gender', 'id_foreign_classes']
    search_fields = ['name_first', 'name_last']

class UnitsInLine(admin.TabularInline):
    model = tblUnits
    extra = 3

class ClassAdmin(admin.ModelAdmin):
    list_display = ('id_classes', 'class_code', 'id_foreign_units')


admin.site.register(tblStudent, StudentAdmin)
admin.site.register(tblClasses, ClassAdmin)
