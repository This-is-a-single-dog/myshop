#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views

app_name = 'seller'
urlpatterns = [
    url(r"register", views.sellerRegister, name="seller_register"),
    url(r"login", views.sellerLogin, name="seller_login"),
    url(r"persional/(\d+)", views.sellerPersional, name="seller_persional"),
    url(r"goodslist/(\d+)", views.sellerAllGoods, name="seller_allGoods"),
    url(r"addgoods/(\d+)", views.sellerAddGoods, name="seller_addGoods"),
    url(r"addtag/(\d+)", views.sellerAddTag, name="seller_addTag"),
    url(r"addpreferential/(\d+)", views.sellerAddPreferential, name="seller_addPreferential"),
    url(r"addtypes/(\d+)", views.sellerAddTypes, name="seller_addTypes"),
    url(r"goodsdetail/(\d+)", views.sellerGoodsDetail, name="seller_goodsDetail"),
    url(r"goodschangemessage/(\d+)", views.sellerGoodsChangeMessage, name="seller_goodsChangeMessage"),
]