from django.contrib import admin
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'image')
    list_filter = ('id', 'category', 'title')
    search_fields = ('title', 'category')
    fields = ('title', 'description', 'category', 'image')
    readonly_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'grade')
    list_filter = ('id', 'grade', 'author', 'product')
    search_fields = ('product', 'grade', 'author', 'product')
    fields = ('author', 'product', 'text', 'grade')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
