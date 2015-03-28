# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=120)),
                ('subject', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=80)),
                ('contributor', models.CharField(max_length=80)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item_type', models.CharField(max_length=80, blank=True)),
                ('item_format', models.CharField(max_length=20)),
                ('identifier', models.CharField(max_length=40)),
                ('source', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=40)),
                ('relation', models.CharField(max_length=40)),
                ('coverage', models.CharField(max_length=80, blank=True)),
                ('rights', models.CharField(max_length=80, blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item_image', models.ImageField(upload_to='items')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TempItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('temp_item', models.ForeignKey(to='collection_item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
