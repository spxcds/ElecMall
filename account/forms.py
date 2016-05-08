# coding=utf-8
from __future__ import unicode_literals
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)


class EditAccountForm(forms.Form):
    email = forms.EmailField(max_length=30)
    phone = forms.CharField(max_length=11)
    mood = forms.CharField(max_length=100)
    role = forms.IntegerField(required=False)
