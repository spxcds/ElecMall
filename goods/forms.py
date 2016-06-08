# coding=utf-8
from __future__ import unicode_literals
from django import forms

class GoodsItemForm(forms.Form):
    id = forms.IntegerField()
    GoodsAmount = forms.IntegerField()
    GoodsName = forms.CharField(max_length=30)
    GoodsPrice = forms.IntegerField()
    BuyNumber = forms.IntegerField()
