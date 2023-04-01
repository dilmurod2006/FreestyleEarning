from django.contrib import admin

from .models import Category, Product, Comment, ProductImage


class WorksImageInline(admin.TabularInline):
    model = ProductImage


class WorksAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('title','category','author', 'price1', 'price2', 'phone_number', 'date')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [WorksImageInline]


admin.site.register(Product, WorksAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ProductImage)
