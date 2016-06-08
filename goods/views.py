# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import View
from utils.shortcuts import info_page

from .models import Goods
from .forms import GoodsItemForm
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
        form = GoodsItemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        try:
            GoodsItem = Goods.objects.get(id=data['id'])
        except GoodsItem.DoesNotExist:
            return info_page(request, '该商品不存在')

        try:
            customer = Customer.objects.get(id=request.user.id)
        except Customer.DoesNotExist:
            return info_page(request, '该用户不存在')

        if data['BuyNumber'] <= 0:
            return info_page(request, '购买的数量需要大于0哦')

        if data['BuyNumber'] > GoodsItem.GoodsAmount:
            return info_page(request, '购买数量超过库存数量')

        if data['BuyNumber'] * data['GoodsPrice'] > customer.Balance:
            return info_page(request, '用户余额不足')

        customer.Balance -= data['BuyNumber'] * data['GoodsPrice']
        customer.save()
        GoodsItem.GoodsAmount -= data['BuyNumber']
        GoodsItem.save();

        return info_page(request, '购买成功')


class UserRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            captcha = Captcha(request)
            if not captcha.check(data['captcha']):
                return info_page(request, '验证码错误')
            try:
                Customer.objects.get(Username=data['Username'])
                return info_page(request, '用户已经存在')
            except Customer.DoesNotExist:
                pass
            try:
                Customer.objects.get(Email=data['Email'])
                return info_page(request, '该邮件已经注册')
            except Customer.DoesNotExist:
                pass
            user = Customer.objects.create(Username=data['Username'], Email=data['Email'], Balance=0,
                                           Telephone=data['Telephone'], Nickname=data['Nickname'], Password=data['Password'])
            request.user = user
            request.session['user_id'] = user.id
            return info_page(request, "注册成功")
        else:
            return info_page(request, "数据格式不合法")

    def get(self, request):
        return render(request, "account/register.html")
