from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Employee


def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html',{'title': "Dashboard"})
def privacyView(request):
    return render(request, 'privacy.html',{'title': "Privacy"})

def employeeView(request):
    all_employee = Employee.objects.all()
    print(all_employee)
    for employee in all_employee:
        print(employee.name)
    return render(request, 'employee.html',{'title': "Blog",'employees' :all_employee})


def loginView(request):
    return render(request, 'login.html',{'title': "Login"})


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm
    return render(request, 'register.html', {'form': form, 'title':"Register Form"})
