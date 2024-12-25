from django.shortcuts import render
from .models import Employee

def employee_list(request):
    emloyees = Employee.objects.all()
    return render(request,'employee_list.html',{'employees':emloyees})

def employee_detail(request,id):
    employee = Employee.objects.get(id=id)
    return render(request,'employee_detail.html',{'employee':employee})
