#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django import forms
from .models import Tag, Types, Seller, Preferential, Goods

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=2)
    password = forms.CharField(widget=forms.PasswordInput)
    sex = forms.fields.ChoiceField(
        choices=((1, "男"),(2, "女"),),
        initial=1,
        widget=forms.widgets.RadioSelect    
    )
    age = forms.CharField()
    phone = forms.CharField(max_length=11)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255)
    photo = forms.FileField(required=False)
    
class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    
class AddGoodsForm(forms.Form):
    name = forms.CharField()
    tagResults = Tag.objects.filter()
    typesResults = Types.objects.filter()
    tags = []
    typess = []
    # 得到所有的标签数据并转换为元组
    if len(tagResults) > 0: # 判断是否为空
        for i in range(0, len(tagResults)):
            result = tagResults[i]
            tag = [result.id, result.name]
            tag = tuple(tag)
            tags.append(tag)
        tags = tuple(tags)
        tag = forms.fields.ChoiceField(
                choices=tags,
                widget=forms.widgets.Select()
            )        
    else:
        pass
    # 得到所有的类型数据并转换为元组
    if len(typesResults) > 0: # 判断是否为空
        for i in range(0, len(typesResults)):
            result = typesResults[i]
            types = [result.id, result.name]
            types = tuple(types)
            typess.append(types)
        typess = tuple(typess)
        types = forms.fields.ChoiceField(
                choices=typess,
                widget=forms.widgets.Select()
            )
    else:
        pass
    # price = forms.CharField(widget=forms.FloatField)
    price = forms.FloatField()
    number = forms.IntegerField()
    color = forms.CharField()
    describe = forms.CharField(widget=forms.Textarea)
    goodsImage = forms.FileField(required=False)
    isPreferential = forms.fields.ChoiceField(
        choices=((1, "是"), (2, "否")),
        initial=2,
        widget=forms.widgets.RadioSelect()
    )

class AddTagForm(forms.Form):
    name = forms.CharField()

class AddTypesForm(forms.Form):
    name = forms.CharField()
    
 
class AddPreferentialForm(forms.Form):
    goodsResults = Goods.objects.filter()
    goodses = []
    if len(goodsResults) > 0: # 判断是否为空
        for i in range(0, len(goodsResults)):
            result = goodsResults[i]
            goods1 = [result.id, result.name]
            goods1 = tuple(goods1)
            goodses.append(goods1)
        goodses = tuple(goodses)
        goods = forms.fields.ChoiceField(
            choices=goodses,
                widget=forms.widgets.Select()
        )
    else:
            pass
    preferential_type = forms.fields.ChoiceField(
        choices=((1, "满减"), (2, "打折"), (3, "满额后打折")),
        initial=1,
        widget=forms.widgets.RadioSelect()
    )
    enoughNumber = forms.FloatField()
    minusNumber = forms.FloatField()
    discount = forms.FloatField()
    cutOffDatetime = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    describe = forms.CharField(widget=forms.Textarea)
