# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect, HttpResponse

from .models import *

# Create your views here.

class UserForm(forms.Form):
    Username = forms.CharField(label='真实姓名', max_length=30)
    Nickname = forms.CharField(label='昵称', max_length=30)
    Telephone = forms.CharField(label='电话', max_length=11)
    Email = forms.EmailField(label='电子邮件')
    Password = forms.CharField(label='密码', widget=forms.PasswordInput())

def index(request):
    context = {}
    return render(request, 'account/index.html', context)

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            Username = uf.cleaned_data['Username']
            Nickname = uf.cleaned_data['Nickname']
            Telephone = uf.cleaned_data['Telephone']
            Email = uf.cleaned_data['Email']
            Password = uf.cleaned_data['Password']

            user = Customer()
            user.Username = Username
            user.Nickname = Nickname
            user.Telephone = Telephone
            user.Email = Email
            user.Password = Password
            user.save()

            return HttpResponse("register successful!")
    else:
        context = {'userform' : UserForm()}
        return render(request, 'account/register.html', context)


def login(request):
    context = {}
    return render(request, 'account/login.html', context)
