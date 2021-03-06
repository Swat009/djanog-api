from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField(unique=True)
    #bio = models.TextField(max_length=500, blank=True)
    mobile_no= models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)
    username=models.CharField(blank=True,null=True,max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email