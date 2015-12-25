# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model('rustic_cut', 'Category')
    Category(name='kitchens').save()
    Category(name='built-ins').save()
    Category(name='tables').save()
    Category(name='furniture').save()
    Category(name='live edge').save()


class Migration(migrations.Migration):

    dependencies = [
        ('rustic_cut', '0002_product_featured'),
    ]

    operations = [
        migrations.RunPython(create_categories)
    ]
