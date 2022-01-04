from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.timezone import now as now
# Create your models here.
from datetime import datetime, date
startTime = datetime.now()
import random        



num = random.randint(1,115) 

class Adding(models.Model):
    
    num1 = models.IntegerField(default=num, blank=True, null=True)
    
    correct = models.CharField(max_length=30, default=0)
    wrong = models.CharField(max_length=30, default=0)
    data = models.DateTimeField(default=now)
    time = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.time

class Star(models.Model):
    add = models.IntegerField(blank=True, null=True)
    sub = models.IntegerField(blank=True, null=True)
    mul = models.IntegerField(blank=True, null=True)
    dev = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.add} {self.user}'
    

