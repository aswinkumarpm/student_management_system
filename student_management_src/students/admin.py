from django.contrib import admin
from .models import Student, StudentMark


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'reporting_teacher')


class StudentMarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'maths_mark', 'science_mark', 'history_mark', 'created', 'updated')


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentMark, StudentMarkAdmin)


