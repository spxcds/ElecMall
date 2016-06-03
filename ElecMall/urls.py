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


    url(r'^goods/index/$', TemplateView.as_view(template_name='goods/index.html')),
    url(r'^goods/Apple/$', TemplateView.as_view(template_name='goods/Apple.html')),
    url(r'^goods/Samsung/$', TemplateView.as_view(template_name='goods/Samsung.html')),
    url(r'^goods/jianeng/$', TemplateView.as_view(template_name='goods/jianeng.html')),
    url(r'^goods/kaxiou/$', TemplateView.as_view(template_name='goods/kaxiou.html')),
    url(r'^goods/hp/$', TemplateView.as_view(template_name='goods/hp.html')),
    url(r'^goods/imac/$', TemplateView.as_view(template_name='goods/imac.html')),
    url(r'^goods/haixin/$', TemplateView.as_view(template_name='goods/haixin.html')),
    url(r'^goods/tcl/$', TemplateView.as_view(template_name='goods/TCL.html')),
    url(r'^goods/lianxiang/$', TemplateView.as_view(template_name='goods/lianxiangyitiji.html')),
    url(r'^goods/hpyitiji/$', TemplateView.as_view(template_name='goods/hpyitiji.html')),
]
