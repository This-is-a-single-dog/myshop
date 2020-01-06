#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import StationAdmin

# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sas = StationAdmin.objects.filter(number=cd['username'])
            # 判断是否为空列表(空报账号不存在，不为空则进行密码比较)
            if len(sas) == 0:
                return HttpResponse("账号不存在！")
            else:
                sa = sas[0]
                if sa.password == cd['password']:
                    return HttpResponse("登录成功")
                else:
                    return HttpResponse("密码不正确！")
        else:
            return HttpResponse("Invalid login")
    
    else:
        form = LoginForm()
        
    return render(request, 'stationAdmin/login.html', {"form": form})
