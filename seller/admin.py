from django.contrib import admin
from .models import Seller, Goods, Tag, Types, Preferential

# Register your models here.
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'age', 'phone', 'email', 'address',]
    
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag', 'types', 'price', 'number', 'time', 'describe', 'isPreferential',]
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ['name']    
    
@admin.register(Preferential)
class PreferentialAdmin(admin.ModelAdmin):
    list_display = ['preferential_type', 'cutOffDatetime', 'describe',]  
