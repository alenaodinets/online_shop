from django.contrib import admin
from catalog.models import Product, Category, Version

# Register your models here.

admin.site.register(Version)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
