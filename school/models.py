from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Parent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField()

    def __str__(self):
        return self.first_name

class Contribution(models.Model):
    contributions = models.CharField(max_length=255)
    parents = models.ManyToManyField(Parent)

    def __str__(self):
        return self.contributions
