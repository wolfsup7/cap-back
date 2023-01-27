from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=32)
    breed = models.CharField(max_length=32)
    age = models.IntegerField()
    picture = models.CharField(max_length=250)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=32)
    appointment = models.CharField(max_length=32)

