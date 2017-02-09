# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def shorten(text):
    "Shorten text to 32 characters."
    if len(text) > 32:
        text = text[:28] + ' ...'
    return text


def revision(text):
    "Try to set the revision off the text."
    # We assume the revision is prepended like this '1) Some text'
    revision = 0
    if ')' in text:
        revision, candidate = text.split(')', 1)
        if revision.isdigit():
            revision = int(revision)
            text = candidate.strip()
        else:
            revision = 0

    revision += 1
    revision = str(revision) + ') '
    return revision + text
    

def migrate(apps, schema_editor):
    """
    Forward migration
    
    The string field 'location' is moved to a many-to-many reference 
    'locations' which therefore needs to be created. The title is shorter than
    the location string in events, therefore we need to shorten it. Which also
    means we need a mechanism to handle false deduplication.
    """
    Event = apps.get_model("glitter_events", "Event")
    Location = apps.get_model("glitter_events", "Location")
    dbi = schema_editor.connection.alias
    
    events_with_locations = Event.objects.using(dbi).filter(location__isnull=False)
    for event in events_with_locations:
        location = event.location
        title = shorten(location)
        try:
            reference = Location.objects.using(dbi).get(location=location)
        except Location.DoesNotExist:
            while Location.objects.using(dbi).filter(title=title).exists():
                title = shorten(revision(title))
                
            reference = Location.objects.using(dbi).create(title=title,
                                                           location=location)

        event.locations.add(reference)


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
