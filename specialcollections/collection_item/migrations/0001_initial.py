# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('subject', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=80)),
                ('contributor', models.CharField(max_length=80)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item_type', models.CharField(blank=True, max_length=80)),
                ('item_format', models.CharField(max_length=20)),
                ('identifier', models.CharField(max_length=40)),
                ('source', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=40)),
                ('relation', models.CharField(max_length=40)),
                ('coverage', models.CharField(blank=True, max_length=80)),
                ('rights', models.CharField(blank=True, max_length=80)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item_image', models.ImageField(upload_to='media/')),
                ('creator', models.ForeignKey(to='collection_user.SCUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TempItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_item', models.ForeignKey(to='collection_item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
