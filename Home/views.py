from django.shortcuts import render
from django.views import View
from .utils import redirect
# Create your views here.


class MyHome(View):
    def get(self,request):
        
        return render(request,"Home/home.html",{
            "fun1":redirect
        })
    

def SingUp(request):
    return render(request,"Home/signup.html")