# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection_item', '0003_auto_20150327_1001'),
        ('collection', '0004_delete_scuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_name', models.CharField(serialize=False, max_length=80, primary_key=True)),
                ('collection_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('item', models.ManyToManyField(to='collection_item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
