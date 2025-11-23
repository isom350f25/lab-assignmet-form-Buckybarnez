from django import forms
from .models import Employee
from .models import Project

class EmployeeForm(forms.ModelForm):
    """
    Form to add/edit an Employee.
    Adjust 'fields' in Meta to match your Employee model fields.
    """
    class Meta:
        model = Employee
        fields = [
            'name',
            'date_of_birth',
            'date_joined',
            'phone_number',
            'position',
        ]
        
class ProjectForm(forms.ModelForm):
    """
    Form to add/edit a Project.
    Adjust 'fields' in Meta to match your Project model fields.
    """
    class Meta:
        model = Project
        fields = [
            'name',
            'start_date',
            'end_date',
            'amount',
            'employee',
        ]