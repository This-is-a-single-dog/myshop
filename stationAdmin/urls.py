#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

app_name = 'stationAdmin'
urlpatterns = [
    url(r"login", views.login, name="stationAdmin_login"),
]