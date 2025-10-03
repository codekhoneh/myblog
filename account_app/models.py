from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    myuser = models.OneToOneField(User,on_delete=models.CASCADE)
    family = models.CharField(max_length=25)
    nationalcode = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/profile',blank=True,null=True)
    def __str__(self):
        return self.myuser.username
# Create your models here.
