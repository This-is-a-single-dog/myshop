#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    registerDate = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to="media/%Y/%m/%d", blank=True, null=True)
    
    class Meta:
        ordering = ('id',)
        index_together = (('id', 'name', 'email'),)
        
    def __str__(self):
        return self.name
    
class Goods(models.Model):
    name = models.CharField(max_length=50) # 货物名称
    tag = models.ForeignKey('Tag', on_delete=models.DO_NOTHING) # 货物标签
    types = models.ForeignKey('Types', on_delete=models.DO_NOTHING) # 货物分类
    price =  models.FloatField()# 货物价格
    number = models.IntegerField() # 货物库存量
    owner = models.ForeignKey('Seller', on_delete=models.DO_NOTHING) # 货物拥有者
    color = models.CharField(max_length=10) # 货物颜色
    time = models.DateField(default=timezone.now) # 货物的上架时间
    describe = models.TextField(max_length=500) # 货物描述
    goodsImage = models.ImageField(upload_to="media/%Y/%m/%d", blank=True, null=True) # 货物图片
    isPreferential = models.CharField(max_length=1, default='否') # 是否打折(值为是或否)
    
    class Meta:
        ordering = ('id',)
        index_together = (('id', 'name'),)
        
    def __str__(self):
        return self.name    
    
class Tag(models.Model):
    name = models.CharField(max_length=10)
    
    class Meta:
        ordering = ('id',)
        index_together = (('id', 'name'),)
        
    def __str__(self):
        return self.name    
    
class Types(models.Model):
    name = models.CharField(max_length=10)
    
    class Meta:
        ordering = ('id',)
        index_together = (('id', 'name'),)
        
    def __str__(self):
        return self.name    
  
class Preferential(models.Model): # 优惠券
    seller = models.ForeignKey('Seller', on_delete=models.DO_NOTHING) # 是哪家店铺发布的优惠券
    goods = models.ForeignKey('Goods', on_delete=models.DO_NOTHING) # 是对那种商品打折
    preferential_type = models.IntegerField() # 优惠类型（满减1、打几折2、满足多少后打几折3）
    enoughNumber =  models.FloatField() # 如果是满减，则此填满多少，不是则填0
    minusNumber =  models.FloatField() # 如果是满减，则此填减多少，不是则填0
    discount =  models.FloatField() # 如果是打折，则此填打折小数（打8折填写0.8），不是则填写1
    cutOffDatetime = models.DateField() # 优惠券的截至日期
    describe = models.TextField(max_length=500) # 优惠券描述
    
    class Meta:
        ordering = ('id',)
        index_together = (('id',),)
        
    def __str__(self):
        return self.describe
    
    
