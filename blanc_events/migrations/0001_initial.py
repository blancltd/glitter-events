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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('published', models.BooleanField(default=True, db_index=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=128)),
                ('summary', models.TextField(help_text='A short sentence description of the event.')),
                ('start', models.DateTimeField(help_text='Start time/date.')),
                ('end', models.DateTimeField(help_text='End time/date.')),
                ('date_url', models.DateField(editable=False, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='blanc_events.Category')),
                ('current_version', models.ForeignKey(null=True, blank=True, to='glitter.Version', editable=False)),
                ('image', blanc_pages.assets.fields.AssetForeignKey(null=True, blank=True, to='assets.Image')),
            ],
            options={
                'ordering': ('start',),
            },
        ),
    ]
