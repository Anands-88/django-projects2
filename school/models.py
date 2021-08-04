from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

class Contribution(models.Model):
    Type = models.CharField(max_length=20)
    parent = models.ManyToManyField(Parent)
    