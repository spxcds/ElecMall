# coding=utf-8
from __future__ import unicode_literals

import urllib
import functools
from functools import wraps
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from utils.shortcuts import info_page
from .models import WuuyunUser


class BasePermissionDecorator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type):
        return functools.partial(self.__call__, obj)

    def __call__(self, *args, **kwargs):
        if len(args) == 2:
            self.request = args[1]
        else:
            self.request = args[0]

        user = self.check_permission()
        if user is not None:
            self.request.wuuyun_user = user
            return self.func(*args, **kwargs)
        else:
            response = HttpResponse("Your role is not admin")
            response.status_code = 302
            response["Location"] = "/login/"
            return response

    def check_permission(self):
        raise NotImplementedError()


class login_required(BasePermissionDecorator):
    def check_permission(self):
        user_id = self.request.session.get("user_id", None)
        if user_id:
            try:
                return WuuyunUser.objects.get(id=user_id)
            except WuuyunUser.DoesNotExist:
                pass
        return None


class admin_required(BasePermissionDecorator):
    def check_permission(self):
        user_id = self.request.session.get("user_id", None)
        if user_id is not None:
            try:
                user = WuuyunUser.objects.get(id=user_id)
                if user.role == 1:
                    return user
            except WuuyunUser.DoesNotExist:
                pass
        return None
