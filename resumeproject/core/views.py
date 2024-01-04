from django.shortcuts import render
from . models import contactmodel



def home(request):
    return render(request,"core/home.html")


def services(request):
    return render(request,'core/services.html')

def skills(request):
    return render(request,'core/skills.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        print(name,email,phone,message)
        obj=contactmodel(name=name,email=email,phone=phone,message=message)
        obj.save()
        return render(request,'core/contact.html')
    return render(request,'core/contact.html')
