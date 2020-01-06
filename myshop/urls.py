"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
# 配置media下的图片
# https://blog.csdn.net/u012561176/article/details/86063128
from django.views.static import serve
from myshop.settings import MEDIA_ROOT
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),    
    url(r'^stationadmin/', include('stationAdmin.urls')),
    url(r'^seller/', include('seller.urls')),
    url(r'index/', views.index, name="index"),
]
