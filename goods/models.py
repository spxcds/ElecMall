from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GOODSCATAGORY(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        db_table = 'goodsCatagory' 
    def __str__(self): 
        return self.name

class Goods(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    GoodsCatagory = models.ForeignKey(GOODSCATAGORY, on_delete=models.CASCADE)
    GoodsAmount = models.PositiveIntegerField()
    GoodsName = models.CharField(max_length=30)
    GoodsPrice = models.IntegerField()
    GoodsPicture = models.ImageField(upload_to='goods')

    class Meta:
        db_table = 'goods' 
    def __str__(self): 
        return self.GoodsName
