from django import forms


class signUpForm(forms.Form):
    Fname=forms.CharField(label="First Name",required=True)
    Lname=forms.CharField(label="Last Name",required=True)
    Mail=forms.EmailField(label="eMail",required=True)
    Phno = forms.CharField(label="Phone no",required=True,max_length=10)


    