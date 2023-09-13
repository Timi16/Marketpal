from django.contrib import admin
from .models import Farmer,Buyer,Product
# Register your models here.
admin.site.register(Farmer)
admin.site.register(Buyer)
admin.site.register(Product)