from django.db import models
class contactmodel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)  
    subject=models.CharField(max_length=100,default='general inquiry')  
    message=models.TextField(max_length=100)
    phone=models.IntegerField()
    

# Create your models here.
