from django.db import models

# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
