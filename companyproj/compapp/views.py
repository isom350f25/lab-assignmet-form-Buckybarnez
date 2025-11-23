from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from .forms import ProjectForm, EmployeeForm

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    today = timezone.now().date()
    projects = employee.projects.filter(start_date__lte=today, 
                                        end_date__gte=today  )
    
    #projects = employee.projects.all()
    return render(request, 'employee_detail.html', 
                  {'employee': employee, 'projects': projects})

def employee_engineers(request):
    employees = Employee.objects.filter(position__icontains="engineer")
    return render(request, 'employee_list.html', {'employees': employees})






from django.shortcuts import render, redirect
from .forms import EmployeeForm

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")  # or any url you have
    else:
        form = EmployeeForm()

    # 👇 THIS sends the form to the template as "form"
    return render(request, "add_employee.html", {"form": form})


def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = ProjectForm()

    return render(request, "add_project.html", {"form": form})



