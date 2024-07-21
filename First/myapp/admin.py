from django.contrib import admin
from .models import Product #First, let's import the product model from models.

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price","isActive","slug",) #It is used to make it appear column-shaped.
    list_display_links=("name","price",)
    readonly_fields=("slug",)
    list_filter=("name","price","category",)
    list_editable=("isActive",)
    search_fields=("name","description",)
admin.site.register(Product,ProductAdmin) #We can store the model information I have defined in the management panel in this way.