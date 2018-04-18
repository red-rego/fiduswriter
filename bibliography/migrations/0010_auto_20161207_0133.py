# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 07:33
from __future__ import unicode_literals

from tornado.escape import json_encode
from django.db import migrations

def modify_entry_cat(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Entry = apps.get_model("bibliography", "Entry")
    for entry in Entry.objects.all():
        entry_cat = []
        if len(entry.entry_cat) > 0:
            cats = entry.entry_cat.split(',')
            for cat in cats:
                entry_cat.append(int(cat))
        entry.entry_cat = json_encode(entry_cat)
        entry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0009_auto_20161207_0130'),
    ]

    operations = [
        migrations.RunPython(modify_entry_cat),
    ]
