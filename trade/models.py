from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    username = models.CharField(max_length=100,blank=False)
    
class postt(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.TimeField(auto_now=False,auto_now_add=False)
    updated_at = models.TimeField(auto_now=False,auto_now_add=False)
    