# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.urlresolvers import reverse

from blanc_pages.admin import BlancPageAdminMixin

from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Event)
class EventAdmin(BlancPageAdminMixin, admin.ModelAdmin):
    pass
    fieldsets = (
        ('Event', {
            'fields': (
                'title', 'category', 'image', 'summary', 'start', 'end'
            )
        }),
        ('Advanced options', {
            'fields': ('slug',)
        }),
    )
    date_hierarchy = 'start'
    list_display = ('title', 'start', 'end', 'category',)
    list_filter = ('published', 'start', 'category')
    prepopulated_fields = {
        'slug': ('title',)
    }
    
    def admin_url(self, obj):
            info = self.model._meta.app_label, self.model._meta.model_name
            redirect_url = reverse('admin:%s_%s_redirect' % info, kwargs={'object_id': obj.id})
            return '<a href="%s">%s</a>' % (redirect_url, 'URL')
    admin_url.short_description = 'URL'
    admin_url.allow_tags = True
    
    
