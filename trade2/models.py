from django.db import models

class product(models.Model):
    name = models.CharField(max_length=100,blank=False)
    weight = models.IntegerField()
    price =models.IntegerField()
    created_at = models.TimeField(auto_now=False,auto_now_add=False)
    updated_at = models.TimeField(auto_now=False,auto_now_add=False)
    
    