from django.contrib import admin
from .models import Menu, Category

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    filter_horizontal = ('item_category',)
    list_display = ['item_name', 'item_price']

admin.site.register(Category)