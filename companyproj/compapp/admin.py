from django.contrib import admin
from .models import Employee, Project

# Register your models here.

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1 #number of epty forms to display

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'date_joined', 'phone_number')
    search_fields = ('name', 'position')
    list_filter = ('position', 'date_joined')
    inlines = [ProjectInline]
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee', 'start_date', 'end_date', 'amount')
    search_fields = ('name', 'employee__name')
    list_filter = ('employee', 'start_date')
    
