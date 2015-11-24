# -*- coding: utf-8 -*-

from django.contrib import admin

from blanc_pages import block_admin
from blanc_pages.admin import BlancPageAdminMixin

from .models import Category, Event, UpcomingEventsBlock


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Event)
class EventAdmin(BlancPageAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('Event', {
            'fields': (
                'title', 'category', 'location', 'image', 'summary', 'start', 'end'
            )
        }),
        ('Advanced options', {
            'fields': ('slug',)
        }),
    )
    date_hierarchy = 'start'
    list_display = ('title', 'start', 'end', 'category',)
    list_filter = ('published', 'start', 'category',)
    prepopulated_fields = {
        'slug': ('title',)
    }


block_admin.site.register(UpcomingEventsBlock)
block_admin.site.register_block(UpcomingEventsBlock, 'Events')
