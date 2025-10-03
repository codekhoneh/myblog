from django.db import models
from django.contrib.auth.models import User

class footer(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

# Create your models here.
