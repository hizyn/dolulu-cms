#coding=utf-8
from django.contrib import admin
from .models import Category, Thing, Post
from django.core.urlresolvers import reverse
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ('title', 'is_nav', 'status')

class ThingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ('title', 'status')

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'description']
    list_display = ('title', 'category', 'status', 'author', 'pub_time')
    filter_horizontal = ('thing',)
    list_filter = ['pub_time']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Thing, ThingAdmin)
admin.site.register(Post, PostAdmin)
