from django.contrib import admin
from .models import Product, Category, Services, Faaliyet,Tag
# Register your models here.


@admin.register(Services)
class ProjeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields={'slug':('title',)}


@admin.register(Faaliyet)
class ProjeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields={'slug':('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields={'slug':('name',)}

@admin.register(Product)
class ProjeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields={'slug':('title',)}
    list_filter=("category",)