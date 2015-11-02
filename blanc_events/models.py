# -*- coding: utf-8 -*-

from django.db import models

from blanc_basic_assets.fields import AssetForeignKey


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blanc-events:category-event-list', (), {
            'slug': self.slug,
        })


class Event(models.Model):
    category = models.ForeignKey('blanc_events.Category')
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = AssetForeignKey('assets.Image', null=True, blank=True)
    image_height = models.PositiveIntegerField(editable=False, null=True)
    image_width = models.PositiveIntegerField(editable=False, null=True)
    summary = models.CharField(
        max_length=100,
        help_text='A short sentence description of the event.'
    )
    description = models.TextField(help_text='All of the event details we have.')

    start = models.DateTimeField(help_text='Start time/date.')
    end = models.DateTimeField(help_text='End time/date.')
    final_date = models.DateTimeField(editable=False, null=True, db_index=True)

    class Meta:
        ordering = ('start',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Set final date to the end, for one off events
        self.final_date = self.end
        super(Event, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('blanc-events:detail', (), {
            'slug': self.slug,
        })


