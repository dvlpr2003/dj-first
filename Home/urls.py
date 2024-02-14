from django.urls import *
from .views import*
urlpatterns = [
    path("",Home),
    path("signup",SingUp,name="sync"),

]