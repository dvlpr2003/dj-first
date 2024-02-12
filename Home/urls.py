from django.urls import *
from .views import*
urlpatterns = [
    path("",MyHome.as_view()),
    path("signup",SingUp,name="sync"),

]