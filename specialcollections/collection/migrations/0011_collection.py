# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection_item', '0006_item_tempitem'),
        ('collection', '0010_auto_20150330_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_name', models.CharField(serialize=False, primary_key=True, max_length=70)),
                ('collection_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
                ('item', models.ManyToManyField(to='collection_item.Item', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
