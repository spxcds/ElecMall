# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import View
from account.decorators import login_required

from utils.shortcuts import info_page
from .forms import UserLoginForm, UserRegisterForm, EditAccountForm
from .models import Customer


class UserRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
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
            Customer.objects.create(Id=None, Username=data['Username'], Email=data['Email'], 
                                    Telephone=data['Telephone'], Nickname=data['Nickname'], Password=data['Password'])
            return info_page(request, "注册成功")
        else:
            return info_page(request, "数据格式不合法")

    def get(self, request):
        return render(request, "account/register.html")


class UserLoginView(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = Customer.objects.get(Email=data["Email"], Password=data["Password"])
                request.session["user_id"] = user.Id
                return info_page(request, "登录成功")
            except WuuyunUser.DoesNotExist:
                return info_page(request, "用户名或密码错误")
        else:
            return info_page(request, "数据格式不合法")

    def get(self, request):
        return render(request, "account/login.html")


'''
class UserLogoutView(View):
    def get(self, request):
        if "user_id" in request.session:
            del request.session["user_id"]
        return info_page(request, "操作成功")


class EditUserView(View):
    @login_required
    def get(self, request):
        return render(request, "account/settings.html")

    @login_required
    def post(self, request):
        form = EditAccountForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.wuuyun_user
            user.email = data["email"]
            user.phone = data["phone"]
            user.mood = data["mood"]
            if data["role"] is None:
                data["role"] = 0
            user.role = data["role"]
            user.save()
            return info_page(request, "编辑成功")
        else:
            return info_page(request, "数据格式不合法")

'''
