from django.db import models


class Thing(models.Model):
    type = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    size = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.IntegerField()
    material = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)


class User(models.Model):
    things = models.ManyToManyField(Thing)
