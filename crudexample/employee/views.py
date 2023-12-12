from django.shortcuts import render ,redirect
from django.template import RequestContext
from employee.forms import EmployeeForm  
from employee.models import Employee  

# Create your views here.
def homeview(request):
   return render (request,'home.html')

def detailsview(request):
   #name = request.post['empname']
   #print(name)
   name=request.post['empname']
   email=request.post['email']
   print(name)
   print(email)
   return render(request,'details.html')

def empformview(request):
   return render(request,'employeeform.html')
#======================================================================================================================
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form}) 

# this will show employee

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

# this will edit an employee with his id
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee}) 

# this will update an employee
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

# this will delete an employee
def delete(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show") 