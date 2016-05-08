# coding=utf-8
from __future__ import unicode_literals
import os
import hashlib
import logging

from django.shortcuts import render


logger = logging.getLogger("app_info")


def info_page(request, text):
    return render(request, "utils/info.html", {"text": text})


def rand_str(length=32):
    if length > 128:
        raise ValueError("length must <= 128")
    return hashlib.sha512(os.urandom(128)).hexdigest()[0:length]