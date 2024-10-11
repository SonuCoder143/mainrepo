from django.shortcuts import render,redirect

# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        return redirect("/login")
    return render(request,"register.html")


def login(request):
    return render(request,"login.html")