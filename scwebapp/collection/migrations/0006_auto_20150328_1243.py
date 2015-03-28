# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='item',
            field=models.ManyToManyField(blank=True, to='collection_item.Item'),
            preserve_default=True,
        ),
    ]
