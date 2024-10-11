from django.shortcuts import render,redirect
from user.models import User

def createUser(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        city=request.POST.get("city")
        print(name,email,city,password)

        userobject=User()
        userobject.name=name
        userobject.email=email
        userobject.password=password
        userobject.city=city
        userobject.save()
        return redirect("/")
    return render(request,"createuser.html")

def index(request):
    return render(request,"index.html")
