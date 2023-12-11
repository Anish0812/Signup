from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from random import*
from django.core.mail import send_mail

def urnp(request):
    if request.user.is_authenticated:
        return redirect("uwelcome")
    else:
        if request.method=="POST":
            un=request.POST.get("un")
            try:
                usr=User.objects.get(username=un)
                pw=randint(10000,99999)
                print(pw)
                usr.set_password(str(pw))
                usr.save()
                subject="Welcome to our website"
                text="User Password is "+str(pw)
                from_email="tester.sumit.2march23@gmail.com"
                to_email=[str(un)]
                send_mail(subject,text,from_email,to_email)
                return redirect("uhome")
            except User.DoesNotExist:
                return render(request,"urnp.html",{"msg":"user not registered"})
        else:
            return render(request,"urnp.html")
def uhome(request):
    if request.user.is_authenticated:
        return redirect("uwelcome")
    else:
        if request.method=="POST":
            un=request.POST.get("un")
            pw=request.POST.get("pw")
            usr=authenticate(username=un,password=pw)
            if usr is None:
                return render(request,"uhome.html",{"msg":"check username/password"})
            else:
                login(request,usr)
                return redirect("uwelcome")
        else:
            return render(request,"uhome.html")
        
def usignup(request):
    if request.user.is_authenticated:
        return redirect("uwelcome")
    else:
        if request.method=="POST":
            un=request.POST.get("un")
            try:
                usr=User.objects.get(username=un)
                return render(request,"usignup.html",{"msg":"email already in use"})
            except User.DoesNotExist:
                pw=randint(10000,99999)
                print(pw)
                usr=User.objects.create_user(username=un,password="1234")
                usr.save()
                subject="Welcome to AZT"
                text="User Password is"+str(pw)
                from_email="tester.sumit.2march23@gmail.com"
                to_email=[str(un)]
                send_mail(subject,text,from_email,to_email)
                return redirect("uhome")
        else:
            return render(request,"usignup.html")
        
def uwelcome(request):
    if request.user.is_authenticated:
        return render(request,"uwelcome.html")
    else:
        return redirect("uhome")
    
def ulogout(request):
    logout(request)
    return redirect("uhome")

