from django.db import models


# Create your models here.

class Stockdata(models.Model):
    date = models.CharField(max_length=20,null = True)
    trade_code = models.CharField(max_length=20)
    high = models.CharField(max_length=20)
    low = models.CharField(max_length=20)
    open = models.CharField(max_length=20)
    close = models.CharField(max_length=20)
    volume = models.CharField(max_length=20)
    
