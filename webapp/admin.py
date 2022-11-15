from django.contrib import admin
from webapp.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'status', 'balance', 'price']
    list_filter = ['status']
    search_fields = ['title']
    exclude = []


admin.site.register(Product, ProductAdmin)