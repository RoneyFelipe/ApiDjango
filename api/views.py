from django.shortcuts import redirect, render
from .models import Employees
from .form import EmployeesForm

# def create(request):
def create(request): 
    data = {}
    form = EmployeesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_reading')

    data['form'] = form
    return render(request,'api/form.html',data)

def read(request):
    data = {}
    data['Employees'] = Employees.objects.all()
    return render(request,'api/reading.html',data)


def update(request,pk):
    data = {}
    employee = Employees.objects.get(pk=pk)
    form = EmployeesForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('url_reading')

    data['form'] = form
    data['employee'] = employee
    return render(request,'api/form.html',data)

def delete(request,pk):
    employee = Employees.objects.get(pk=pk)
    employee.delete()
    return redirect('url_reading')

# def delete(request):
# Create your views here.
