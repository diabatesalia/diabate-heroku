from re import A
from django.contrib import admin
from shop.models import Product, Category

# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_ajou')

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'date_ajou')


admin.site.register(Category, AdminCategorie)
admin.site.register(Product, AdminProduct)
