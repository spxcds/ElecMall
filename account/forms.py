# coding=utf-8
from __future__ import unicode_literals
from django import forms

class UserLoginForm(forms.Form):
    Email = forms.CharField(max_length=30)
    Password = forms.CharField(max_length=20)


class UserRegisterForm(forms.Form):
    Username = forms.CharField(max_length=30)
    Nickname = forms.CharField(max_length=30)
    Telephone = forms.CharField(max_length=11)
    Email = forms.EmailField(max_length=30)
    Password = forms.CharField(max_length=20)


class UserEditForm(forms.Form):
    Username = forms.CharField(max_length=30)
    Nickname = forms.CharField(max_length=30)
    Telephone = forms.CharField(max_length=11)
    Email = forms.EmailField(max_length=30)
