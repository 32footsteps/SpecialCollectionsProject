# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_item', '0002_item_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
