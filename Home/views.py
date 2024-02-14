from django.shortcuts import render
from django.views import View
from .utils import redirect
from .form import signUpForm

def Home(request):
        
    return render(request,"Home/home.html",{
        "fun1":redirect
    })
    

def SingUp(request):
    newForm = signUpForm()
    return render(request,"Home/signup.html",{
        "form":newForm
    })
