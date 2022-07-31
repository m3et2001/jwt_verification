from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    username = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number=models.IntegerField(blank=True,null=True)
    birth_date=models.DateField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','username','phone_number','birth_date']
    