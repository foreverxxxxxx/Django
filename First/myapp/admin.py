
from django.contrib import admin
from .models import Category, Product, Supplier ,Address #First, let's import the product model from models.

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price","isActive","slug","selected_categories",) #It is used to make it appear column-shaped.
    list_display_links=("name","price",)
    # readonly_fields=("slug",)
    prepopulated_fields={"slug":("name",)}
    list_filter=("name","price","categories")
    list_editable=("isActive",)
    search_fields=("name","description",)
    def selected_categories(self,obj):
        html=""
        for category in obj.categories.all():
            html +=category.name + " "

        return html

  



admin.site.register(Product,ProductAdmin) #We can store the model information I have defined in the management panel in this way.
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Address)