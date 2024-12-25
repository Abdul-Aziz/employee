from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'date_of_field','gender','skills','state','city','profile_picture','resume','video')
# Register your models here.
