from django.contrib import admin
from django.contrib.auth.models import User, Group as auth_group
from olcha.models import Category, Group, Image, Product

# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'slug']
    prepopulated_fields = {'slug': ('group_name',)}


@admin.register(Product)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'price', 'quantity', 'rating', 'discount', 'slug', 'group']
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Image)
admin.site.unregister(User)
admin.site.unregister(auth_group)

