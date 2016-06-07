from django.contrib import admin

# Register your models here.

from .models import Goods, GOODSCATAGORY

admin.site.register(Goods)
admin.site.register(GOODSCATAGORY)
