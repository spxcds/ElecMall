from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    Balance = models.IntegerField(default=0)
    Username = models.CharField(max_length=30)
    Nickname = models.CharField(max_length=30)
    Telephone = models.CharField(max_length=11)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=20)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.Nickname
