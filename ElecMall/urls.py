"""ElecMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views
from django.views.generic import TemplateView
from account.views import UserRegisterView, UserLoginView, UserLogoutView, UserEditView
from utils.captcha.views import show_captcha

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/register/$', UserRegisterView.as_view()),
    url(r'^account/login/$', UserLoginView.as_view()),
    url(r'^account/logout/$', UserLogoutView.as_view()),
    url(r'^account/settings/$', UserEditView.as_view()),
    url(r'^goods/show/$', TemplateView.as_view(template_name='goods/demo.html')),
    url(r'^captcha/$', show_captcha),


    url(r'^goods/phone/$', TemplateView.as_view(template_name='ElecMall/index.html')),
    url(r'^goods/camera/$', TemplateView.as_view(template_name='ElecMall/index.html')),
    url(r'^goods/notebook/$', TemplateView.as_view(template_name='ElecMall/index.html')),
    url(r'^goods/tv/$', TemplateView.as_view(template_name='ElecMall/index.html')),
    url(r'^goods/all_in_one/$', TemplateView.as_view(template_name='ElecMall/index.html')),
]
