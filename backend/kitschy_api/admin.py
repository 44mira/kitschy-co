from django.contrib import admin

from kitschy_api.models import Product, ProductImage, User

admin.site.register(User)


class ProductImageInline(
    admin.TabularInline
):  # or admin.StackedInline for a different layout
    model = ProductImage
    extra = 1  # Number of empty forms to display


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "status", "category"]
    inlines = [ProductImageInline]


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["product_image_id", "product", "alt_desc"]


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
