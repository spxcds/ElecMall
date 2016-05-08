from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    Id = models.CharField(max_length=32, primary_key=True, db_index=True)
    Username = models.CharField(max_length=30)
    Nickname = models.CharField(max_length=30)
    Telephone = models.CharField(max_length=11)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=20)

    class META:
        db_table = 'customer'

    def __str__(self):
        return self.Nickname
