from django.db import models
from django.contrib.auth.models import User


class Monitores(models.Model):
    nombre= models.CharField(max_length=50, unique=True)
    precio= models.IntegerField()
    cantidad= models.IntegerField()
    tamaño= models.IntegerField()
    imagen= models.ImageField(null=True, blank=True, upload_to="media/")
    descripcion= models.CharField(max_length=400, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    

class Amplificadores(models.Model):
    nombre= models.CharField(max_length=50, unique=True)
    precio= models.IntegerField()
    cantidad= models.IntegerField()
    potencia= models.IntegerField()
    imagen= models.ImageField(null=True, blank=True, upload_to="media/")
    descripcion= models.CharField(max_length=400, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Notebooks(models.Model):
    nombre= models.CharField(max_length=50, unique=True)
    precio= models.IntegerField()
    cantidad= models.IntegerField()
    imagen= models.ImageField(null=True, blank=True, upload_to="media/")
    descripcion= models.CharField(max_length=400, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


