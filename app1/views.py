from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponseRedirect

def employee_list(request):
    emloyees = Employee.objects.all()
    return render(request,'employee_list.html',{'employees':emloyees})

def employee_detail(request,id):
    employee = Employee.objects.get(id=id)
   # employee =get_object_or_404(employee,id=id)
    return render(request,'employee_detail.html',{'employee':employee})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:   
        form = EmployeeForm()

    return render(request,"employee_add.html",{'form':form})
