# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import View
from utils.shortcuts import info_page
from account.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm, EditAccountForm
from .models import WuuyunUser


class UserRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                WuuyunUser.objects.get(username=data["username"])
                return info_page(request, "用户名已经存在")
            except WuuyunUser.DoesNotExist:
                pass
            try:
                WuuyunUser.objects.get(email=data["email"])
                return info_page(request, "email已经存在")
            except WuuyunUser.DoesNotExist:
                pass
            WuuyunUser.objects.create(username=data["username"], email=data["email"], password=data["password"])
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
                user = WuuyunUser.objects.get(username=data["username"], password=data["password"])
                request.session["user_id"] = user.id
                return info_page(request, "登录成功")
            except WuuyunUser.DoesNotExist:
                return info_page(request, "用户名或密码错误")
        else:
            return info_page(request, "数据格式不合法")

    def get(self, request):
        return render(request, "account/login.html")


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

