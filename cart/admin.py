from django.contrib import admin

from cart.models import CartItem, Order
from .migrations import *
# Register your models here.

admin.site.register(Order)
admin.site.register(CartItem)