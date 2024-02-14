from django.db import models

class Name(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.fName}.{self.lName}"
class User(models.Model):
    Name = models.OneToOneField(Name,on_delete=models.CASCADE)
    Mail = models.EmailField(max_length=100,)
    password = models.CharField(max_length=100,null=True)