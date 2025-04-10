from django.db import models

# Create your models here.
class Item1(models.Model): # for df1
    name = models.CharField(max_length = 255)
    date_time = models.CharField(max_length = 255)

class Item2(models.Model): # for df2
    name = models.CharField(max_length = 255)
    date_time = models.CharField(max_length = 255)
