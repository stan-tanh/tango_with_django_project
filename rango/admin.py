from contextlib import ContextDecorator
from multiprocessing import context
from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAmdin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAmdin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
