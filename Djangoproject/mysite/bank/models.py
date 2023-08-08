from django.db import models

# create your models here.
class AccountHolder(models.Model):
    name=models.CharField(max_length=30)
    Mobile=models.BigIntegerField(default="")
    balance=models.FloatField(default=8)
    password=models.CharField(max_length=30)