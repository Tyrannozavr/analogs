from django.contrib import admin
# from models import Products
from Analogs.models import Products, Analogs, Images

class ImagesInline(admin.TabularInline):
    model = Images.products.through


class ProductInlines(admin.StackedInline):
    model = Products
    extra = 5

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


class AnalogsAdmin(admin.ModelAdmin):
    inlines = [
        ProductInlines,
               ]

admin.site.register(Analogs, AnalogsAdmin)