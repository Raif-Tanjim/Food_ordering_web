from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    Number = models.CharField(max_length=14,unique=True)
    email = models.EmailField(unique=True)
    user_Img = models.ImageField(upload_to="Profile")
    USERNAME_FIELD = 'Number'
    REQUIRED_FIELDS = []
   
    objects = UserManager()
    
   