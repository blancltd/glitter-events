# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0002_owner_optional'),
        ('blanc_events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingEventsBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('category', models.ForeignKey(null=True, blank=True, to='blanc_events.Category')),
                ('content_block', models.ForeignKey(editable=False, null=True, to='glitter.ContentBlock')),
            ],
            options={
                'verbose_name': 'upcoming events',
            },
        ),
    ]
