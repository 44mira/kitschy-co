from django.contrib import admin
from kitschy_api.models import Product, ProductImage, User, Address, CartItem, Cart, OrderItems, Order


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'membership_id', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']
    list_filter = ['is_active', 'is_staff']
    inlines = [AddressInline]

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'user', 'region', 'city', 'postal_code', 'barangay']
    search_fields = ['user__email', 'region', 'city', 'barangay']
    list_filter = ['region', 'city']

admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)

class ProductImageInline(admin.StackedInline):  
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'price', 'quantity', 'status', 'category']
    search_fields = ['name', 'desc']
    list_filter = ['status', 'category']
    filter_horizontal = ['creators']
    inlines = [ProductImageInline]

    fieldsets = [
        (None, {
            'fields': ['name', 'desc', 'price', 'quantity', 'status', 'category', 'creators']
        }),
    ]

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product_image_id', 'product', 'img_url', 'alt_desc']
    search_fields = ['product__name', 'alt_desc']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)

# Cart and CartItem
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'user', 'created_at', 'updated_at']
    search_fields = ['user__email']
    list_filter = ['created_at']
    inlines = [CartItemInline]

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'cart', 'product', 'quantity']
    search_fields = ['product__name']

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

# Order and OrderItems
class OrderItemInline(admin.TabularInline):
    model = OrderItems
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'method', 'status', 'delivery_date', 'created_at']
    search_fields = ['user__email', 'order_id']
    list_filter = ['status', 'method', 'delivery_date']
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'order', 'product', 'quantity', 'created_at']
    search_fields = ['order__order_id', 'product__name']
    list_filter = ['created_at']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems, OrderItemAdmin)