# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('glitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('image_height', models.PositiveIntegerField(null=True, editable=False)),
                ('image_width', models.PositiveIntegerField(null=True, editable=False)),
                ('summary', models.TextField(help_text='A short sentence description of the event.')),
                ('start', models.DateTimeField(help_text='Start time/date.')),
                ('end', models.DateTimeField(help_text='End time/date.')),
                ('final_date', models.DateTimeField(null=True, editable=False, db_index=True)),
                ('published', models.BooleanField(default=True, help_text='Post will be hidden unless this option is selected', db_index=True)),
                ('date_url', models.DateField(editable=False, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='blanc_events.Category')),
                ('current_version', models.ForeignKey(blank=True, editable=False, to='glitter.Version', null=True)),
                ('image', blanc_basic_assets.fields.AssetForeignKey(blank=True, to='assets.Image', null=True)),
            ],
            options={
                'ordering': ('start',),
                'permissions': (('edit_page', 'Can edit page'), ('publish_page', 'Can publish page'), ('view_protected_page', 'Can view protected page')),
            },
        ),
    ]
