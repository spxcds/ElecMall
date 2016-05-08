from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    Username = models.CharField(max_length=30)
    Nickname = models.CharField(max_length=30)
    Telephone = models.CharField(max_length=11)
    Email = models.EmailField
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Nickname
