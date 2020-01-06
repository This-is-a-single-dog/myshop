#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import RegisterForm, LoginForm, AddGoodsForm, AddTagForm, AddTypesForm, AddPreferentialForm
from .models import Seller, Tag, Types, Goods, Preferential

# Create your views here.
def sellerRegister(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            if cd['sex'] == 1:
                sex = '男'
            else:
                sex = '女'
            age = cd['age']
            phone = cd['phone']
            email = cd['email']
            address = cd['address']
            photo = request.FILES.get("photo")
            seller = Seller()
            seller.name = username
            seller.password = password
            seller.sex = sex
            seller.age = age
            seller.phone = phone
            seller.email = email
            seller.address = address
            seller.photo = photo
            seller.save()
            return HttpResponse("success")
        else:
            return HttpResponse("Invalid register")
    
    else:
        form = RegisterForm()
        
    return render(request, 'seller/register.html', {"form": form})

def sellerLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)    
        if form.is_valid():
            cd = form.cleaned_data
            phone = cd['phone']
            password = cd['password']
            sellers = Seller.objects.filter(phone=phone)
            if len(sellers) == 0:
                return HttpResponse("账号不存在！")
            else:
                seller = sellers[0]
                if password == seller.password:
                    # return HttpResponse("登录成功！")
                    response = redirect('/seller/persional/' + str(seller.id))
                    #设置cookie username *过期时间为12小时， 设置一个星期为：7*24*3600
                    response.set_cookie('username', seller, max_age=1*12*3600)
                    request.session['islogin'] = True
                    return response
                else:
                    return HttpResponse("密码错误！")
            
    else:
        form = LoginForm()
        
    return render(request, 'seller/login.html', {"form": form})

def sellerPersional(request, id):
    if request.session.has_key('islogin'): # 检测是否登录
        sellers = Seller.objects.filter(id=id)
        seller = sellers[0]
        data = {}
        
        data['seller'] = seller
        
        return render(request, 'seller/persional.html', data)
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form}) 
    
def sellerAllGoods(request, id):
    if request.session.has_key('islogin'): # 检测是否登录
        goodses = Goods.objects.filter(owner_id=id)
        data = {}
        
        data['goodses'] = goodses
        
        return render(request, 'seller/goodslist.html', data)
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form})    
    
def sellerAddGoods(request, id):
    if request.session.has_key('islogin'): # 检测是否登录
        if request.method == "POST":
            form = AddGoodsForm(request.POST)    
            if form.is_valid():
                cd = form.cleaned_data
                # 提取从表单中传过来的数据并进行处理
                name = cd['name']
                formTag = cd['tag']
                formTypes = cd['types']
                price = cd['price']
                number = cd['number']
                color = cd['color']
                describe = cd['describe']
                print(describe)
                tag = Tag.objects.filter(id=formTag)[0]
                types = Types.objects.filter(id=formTypes)[0]
                owner = Seller.objects.filter(id=id)[0]
                goodsImage = request.FILES.get("goodsImage")
                # 创建数据并插入数据库
                goods = Goods()
                goods.name = name
                goods.tag = tag
                goods.types = types
                goods.price = price
                goods.number = number
                goods.owner = owner
                goods.color = color
                goods.describe = describe
                print("des:", goods.describe)
                goods.goodsImage = goodsImage
                goods.save()
        else:
            form = AddGoodsForm()
            
        return render(request, 'seller/addgoods.html', {"form": form})
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form}) 
    
def sellerAddTag(request, id):
    if request.session.has_key('islogin'): # 检测是否登录
        if request.method == "POST":
            form = AddTagForm(request.POST)    
            if form.is_valid():
                cd = form.cleaned_data
                name = cd['name']
                tag = Tag()
                tag.name = name
                tag.save()
        else:
            form = AddTagForm()
            
        return render(request, 'seller/addtag.html', {"form": form})
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form}) 
    
def sellerAddTypes(request, id):
    if request.session.has_key('islogin'): # 检测是否登录
        if request.method == "POST":
            form = AddTypesForm(request.POST)    
            if form.is_valid():
                cd = form.cleaned_data
                name = cd['name']
                types = Types()
                types.name = name
                types.save()
        else:
            form = AddTypesForm()
            
        return render(request, 'seller/addtypes.html', {"form": form})
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form}) 
    
def sellerGoodsDetail(request, id):
    if request.session.has_key('islogin'): # 检测是否登录
        goods = Goods.objects.get(id=id)
        data = {}
        data['goods'] = goods
        if goods.isPreferential == '是':
            seller = Seller.objects.get(id=goods.owner_id)
            preferentials = Preferential.objects.filter(seller_id=seller.id).filter(goods_id=goods.id)
            data['preferentials'] = preferentials
        
        return render(request, 'seller/goodsdetail.html', data)
    
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form})     
    
def sellerGoodsChangeMessage(request, id):
    if request.session.has_key('islogin'):
        if request.method == "POST":
            form = AddGoodsForm(request.POST)    
            if form.is_valid():
                goods = Goods.objects.get(id=id)                
                cd = form.cleaned_data
                # 提取从表单中传过来的数据并进行处理
                name = cd['name']
                formTag = cd['tag']
                formTypes = cd['types']
                price = cd['price']
                number = cd['number']
                color = cd['color']
                describle = cd['describle']
                print(describle)
                tag = Tag.objects.filter(id=formTag)[0]
                types = Types.objects.filter(id=formTypes)[0]
                goodsImage = request.FILES.get("goodsImage")
                # 创建数据并插入数据库
                goods.name = name
                goods.tag = tag
                goods.types = types
                goods.price = price
                goods.number = number
                goods.color = color
                goods.describle = describle
                print("des:", goods.describe)
                goods.goodsImage = goodsImage
                goods.save()
        else:
            form = AddGoodsForm()
            
        return render(request, 'seller/goodschangemessage.html', {"form": form})
    
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form})
    
def sellerAddPreferential(request, id): # 传入的是seller的id
    if request.session.has_key('islogin'):
        if request.method == "POST":
            form = AddPreferentialForm(request.POST)    
            if form.is_valid():
                cd = form.cleaned_data
                goods = Goods.objects.get(id=cd['goods'])
                preferential_type = cd['preferential_type']
                enoughNumber = cd['enoughNumber']
                minusNumber = cd['minusNumber']
                discount = cd['discount']
                cutOffDatetime = cd['cutOffDatetime']
                describe = cd['describe']
                seller = Seller.objects.get(id=id)
                if int(preferential_type) > 0 and int(preferential_type) < 3:
                    preferential = Preferential()
                    goods.isPreferential = '是'
                    goods.save()
                    preferential.goods = goods
                    preferential.seller = seller
                    preferential.preferential_type = preferential_type
                    preferential.enoughNumber = enoughNumber
                    preferential.minusNumber = minusNumber
                    preferential.discount = discount
                    preferential.cutOffDatetime = cutOffDatetime
                    preferential.describe = describe
                    preferential.save()
        else:
            form = AddPreferentialForm()
            
        return render(request, 'seller/addpreferential.html', {"form": form})        
    
    else:
        form = LoginForm()
        return render(request, 'seller/login.html', {"form": form})        
