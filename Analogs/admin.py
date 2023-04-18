from django.contrib import admin
# from models import Products
from Analogs.models import Products, Analogs, Images

class ImagesInlines(admin.TabularInline):
    model = Images.products.through
class ProductInlines(admin.StackedInline):
    model = Products
    extra = 5

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'analogs',)
    fields = ('name', 'analogs', '_analogs')
    readonly_fields = ('analogs',)



class AnalogsAdmin(admin.ModelAdmin):
    inlines = [ProductInlines,
               ImagesInlines
               ]

admin.site.register(Analogs, AnalogsAdmin)