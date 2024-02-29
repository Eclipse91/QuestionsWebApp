from django.db import models

# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)