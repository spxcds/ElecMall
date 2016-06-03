from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Goods(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    GoodsCatagory = models.CharField(max_length=20);
    GoodsAmount = models.PositiveIntegerField()
    GoodsName = models.CharField(max_length=30)
    GoodsPrice = models.CharField(max_length=30)
    GoodsPicture = models.ImageField()

    class Meta:
        db_table = 'goods' 
    def __str__(self): 
        return self.GoodsName
