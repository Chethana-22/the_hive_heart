from django.contrib import admin

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(artist)
admin.site.register(painting)
admin.site.register(Art)
admin.site.register(Photography)
admin.site.register(customer)