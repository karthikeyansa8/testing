from django.db import models

# Create your models here.

class testform(models.Model):
    name = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    password = models.TextField()
    
    