# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


