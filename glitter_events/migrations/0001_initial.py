# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blanc_pages.assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('published', models.BooleanField(db_index=True, default=True)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('location', models.CharField(max_length=128, blank=True)),
                ('summary', models.TextField(help_text='A short sentence description of the event.')),
                ('start', models.DateTimeField(help_text='Start time/date.')),
                ('end', models.DateTimeField(help_text='End time/date.')),
                ('date_url', models.DateField(db_index=True, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='blanc_events.Category')),
                ('current_version', models.ForeignKey(editable=False, to='glitter.Version', null=True, blank=True)),
                ('image', blanc_pages.assets.fields.AssetForeignKey(to='assets.Image', null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'ordering': ('start',),
                'default_permissions': ('add', 'change', 'delete', 'edit', 'publish'),
            },
        ),
    ]
