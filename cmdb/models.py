from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    tel=models.CharField(max_length=12)
class Show(models.Model):
    name=models.TextField(max_length=1000)
    shopname = models.TextField(max_length=1000,default='')
    price=models.DecimalField(max_digits=8,decimal_places=2)
    pinglun=models.IntegerField()
    hit=models.IntegerField(default=0)

