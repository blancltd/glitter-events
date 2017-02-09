# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('glitter_events', '0004_add_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, db_index=True)),
                ('location', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='locations',
            field=models.ManyToManyField(blank=True, to='glitter_events.Location'),
        ),
        migrations.RunPython(
            migrate,
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
    ]
