from django.contrib import admin
from .models import StudentNew


@admin.register(StudentNew)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','email')