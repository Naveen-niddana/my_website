from django.contrib import admin
from .models import Products,Offer


class ProductsAdmin(admin.ModelAdmin):
    list_display=('name','stock','price')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')


admin.site.register(Offer,OfferAdmin)
admin.site.register(Products,ProductsAdmin)
