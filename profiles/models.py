from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Farmer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farmer')
    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='buyer')
    def __str__(self):
        return self.user.username
        
class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE) 
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
   
   
   
   
