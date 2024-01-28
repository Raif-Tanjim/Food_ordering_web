from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    firstName = models.CharField(max_length=30, blank=True, null=True)
    lastName = models.CharField(max_length=30, blank=True, null=True)
    number = models.CharField(max_length=11, unique=True, null=True)
    Email = models.EmailField(unique=True, null=True, blank=True)
    Address = models.TextField(default='address', blank=True, null=True)
    user_img = models.ImageField(upload_to="Profile")
    city = models.CharField(max_length=255, default='city', blank=True, null=True)
