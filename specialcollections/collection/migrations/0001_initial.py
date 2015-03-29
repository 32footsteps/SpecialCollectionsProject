# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_user', '0001_initial'),
        ('collection_item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_name', models.CharField(primary_key=True, serialize=False, max_length=80)),
                ('collection_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to='collection_user.SCUser')),
                ('item', models.ManyToManyField(blank=True, to='collection_item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
