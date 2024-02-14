from django import forms


class signUpForm(forms.Form):
    Fname=forms.CharField(label="First Name",required=True)
    Lname=forms.CharField(label="Last Name",required=True)
    Mail=forms.EmailField(label="eMail",required=True)
    password = forms.CharField(label="Password",required=True)
    c_password =forms.CharField(label="Confirm Password",required=True)

class LoginForm(forms.Form):
    Mail = forms.EmailField(label="Mail",required=True)
    Password = forms.CharField(label="Password",required=True)


    