from django.shortcuts import render
from django.views import View
from .utils import redirect
from .form import signUpForm,LoginForm
from.models import *
class SignUp(View):
    def get(self,request):
        form = signUpForm()
        return render(request,"Home/signup.html",{
            "form":form
        })
    def post(self,request):
        form=signUpForm(request.POST)
        if form.is_valid():
            name =Name(fName=form.cleaned_data["Fname"],lName=form.cleaned_data["Lname"])
            name.save()
            usr = User(Name=name,Mail=form.cleaned_data['Mail'],password =form.cleaned_data['password'])
            usr.save()
            return render(request,"Home/home.html")
        return render(request,"Home/signup.html",{
            'form':form
        })
    
def LogIn(request):
    form = LoginForm()
    return render(request,"Home/Login.html",{
        'form':form
    })