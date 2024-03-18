from django.contrib import admin

from fashion.models import Item, Category


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
