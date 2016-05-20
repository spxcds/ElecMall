from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Goods(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    Goodsamount = models.PositiveIntegerField()
    Goodsname = models.CharField(max_length=30)
    Goodsprice = models.CharField(max_length=30)
    Goodpicture = models.ImageField()

    class Meta:
        db_table = 'goods' 
    def __str__(self): 
        return self.Goodsname
