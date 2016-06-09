from __future__ import unicode_literals

from django.db import models

from account.models import Customer

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

class Order(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    Order_time = models.DateTimeField(auto_now=True)
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    Goods_num = models.IntegerField()
    Goods_price = models.IntegerField()
    Order_total = models.IntegerField()

    class Meta:
        db_table = 'order'
    def __str__(self): 
        return self.id

