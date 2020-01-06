#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html', {})