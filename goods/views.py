# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import View
from utils.shortcuts import info_page

from .models import Goods
from account.decorators import login_required
from account.models import Customer

class GoodsShowView(View):

    def get(self, request, catagory):
        try:
            user_id = request.session.get("user_id", None)
            request.user = Customer.objects.get(id=user_id)
        except Customer.DoesNotExist:
            pass

        goods = Goods.objects.filter(GoodsCatagory=catagory)
        if not goods:
            return info_page(request, "没有此类商品")
        context = {'goods': goods}
        return render(request, 'goods/index.html', context)


class GoodsShowItemView(View):

    def get(self, request, goods_id):
        try:
            user_id = request.session.get("user_id", None)
            request.user = Customer.objects.get(id=user_id)
        except Customer.DoesNotExist:
            pass

        try:
            item = Goods.objects.get(id=goods_id)
        except:
            return info_page(request, "没有此商品")
        context = {'item': item}
        return render(request, 'goods/item.html', context)

    @login_required
    def post(self, request, goods_id):
        return info_page(request, '其实, 你已经登录成功了')
