import rustic_cut.models as m

from django.contrib.admin.views.main import ChangeList
from django.contrib import admin


@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'categories')

    
@admin.register(m.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)