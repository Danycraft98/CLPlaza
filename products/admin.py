from django.contrib import admin

# Register your models here.
from .models import *


class TagInline(admin.TabularInline):
    model = Tag
    extra = 2


class ProductInline(admin.TabularInline):
    model = Product
    extra = 2


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 2


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name']})]
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['name']}),
        ('details', {'fields': ['category', 'price', 'stock']})
    )
    inlines = [ImageInline]


#class ProductAdmin(admin.ModelAdmin):
#    fieldsets = [(None, {'fields': ['content']})]
#    inlines = [TagInline]


admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
