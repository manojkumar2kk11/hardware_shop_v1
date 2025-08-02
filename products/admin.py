from django.contrib import admin
from .models import Product, Category, Tag

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'display_tags',
    )

    ordering = ('sku',)
    filter_horizontal = ('tags',)  # adds the multi-select widget for tags

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    display_tags.short_description = 'Tags'

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)