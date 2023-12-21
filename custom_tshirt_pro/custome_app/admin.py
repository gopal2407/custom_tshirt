from django.contrib import admin

from .models import Customer, Owner, Address, Category, ItemType, Coupon, Color, ItemSize
from .models import Item, SubCategory, OrderMaster, OrderedItem, Font

admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(ItemType)
admin.site.register(Coupon)
admin.site.register(Color)
admin.site.register(ItemSize)
admin.site.register(Item)
admin.site.register(SubCategory)
admin.site.register(OrderMaster)
admin.site.register(OrderedItem)
admin.site.register(Font)
