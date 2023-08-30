from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50,primary_key=True,unique=True)
    Number = models.IntegerField()
    email= models.EmailField(max_length=254)
