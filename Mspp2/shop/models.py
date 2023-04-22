from django.db import models
from datetime import datetime
import django
from django_mysql.models import ListCharField


# Create your models here.
class Image(models.Model):
    jio=[
        ('pp',"product"),
        ('ss',"service")
    ]
    jid=models.CharField(max_length=12)
    name=models.CharField(max_length=12)
    price=models.IntegerField(default=0)
    Type=models.CharField(max_length=2,choices=jio ,null=True,default=None)
    imo=models.ImageField(upload_to="images",default=True)
    desc=models.TextField(max_length=200,default="o")
    def __str__(self):
        return self.name
class Orders(models.Model):
    user=models.CharField(max_length=40,default="anonymous")
    approved=models.BooleanField(default=False)
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    city=models.CharField(max_length=120)
    Tracker=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=120)
    zip_code=models.CharField(max_length=120)
    items=models.CharField( max_length=550)
    order_id=models.CharField(max_length=120,default='899')
    def __str__(self):
        return self.name


