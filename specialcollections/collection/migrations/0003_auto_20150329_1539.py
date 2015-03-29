# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20150329_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='author',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
