# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20150330_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='collection_name',
            field=models.CharField(max_length=70, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
