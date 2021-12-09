from django.shortcuts import render
from .models import EmpModel
from django.contrib import messages

def shoemp(request):
    empmodels = EmpModel.objects.all()
    return render(request,'index.html',{'empmodels':empmodels})

def insertemp(request):
    if request.method == "POST":
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('salary') and  request.POST.get('gender'):
             saverecord =  EmpModel()
             saverecord.empname=  request.POST.get('empname')
             saverecord.email =  request.POST.get('email')
             saverecord.occupation = request.POST.get('occupation')
             saverecord.salary = request.POST.get('salary')
             saverecord.gender = request.POST.get('gender')
             print(saverecord.occupation)
             saverecord.save()
             messages.success(request,'employee'+ saverecord.empname + 'added')
             return render(request,'insert.html')
    else:
        return render(request,'insert.html') 