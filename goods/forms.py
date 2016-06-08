# coding=utf-8
from __future__ import unicode_literals
from django import forms

class GoodsItemForm(forms.Form):
    GoodsAmount = forms.IntegerField()
    GoodsName = forms.CharField(max_length=30)
    GoodsPrice = forms.CharField(max_length=30)
    BuyNumber = forms.IntegerField()
