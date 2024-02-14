from django.urls import *
from .views import*
urlpatterns = [
    path("signup",SignUp.as_view(),name="onreq"),
    path("login",LogIn)

]