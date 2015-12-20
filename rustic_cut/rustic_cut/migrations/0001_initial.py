# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=2096)),
                ('photo', models.ImageField(null=True, upload_to=b'static/rustic_cut/img/product-photos', blank=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(related_name='products', to='rustic_cut.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
