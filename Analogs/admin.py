from django.contrib import admin
# from models import Products
from Analogs.models import Products, Analogs



class ProductInlines(admin.StackedInline):
    model = Products

    extra = 5

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'analogs',)
    fields = ('name', 'analogs', '_analogs')
    readonly_fields = ('analogs',)



class AnalogsAdmin(admin.ModelAdmin):
    inlines = [ProductInlines]

admin.site.register(Analogs, AnalogsAdmin)