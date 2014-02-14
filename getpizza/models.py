from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    login = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

class Pizza(models.Model):

    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    image = models.ImageField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Wallet(models.Model):

    count = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    def __init__(self):
        return self.total_price



