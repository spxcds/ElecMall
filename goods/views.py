# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import View
from utils.shortcuts import info_page

from .models import Goods

class GoodsShowView(View):

    def get(self, request, catagory):
        goods = Goods.objects.filter(GoodsCatagory=catagory)
        context = {'goods': goods}
        return render(request, 'goods/index.html', context)
