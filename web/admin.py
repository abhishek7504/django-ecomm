from django.contrib import admin
from .models import Product,Category,Wishlist

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title","available","price","added_on",)
    list_filter = ("available",)
    search_fields = ("title", )
    readonly_fields = ("added_on", )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user",)