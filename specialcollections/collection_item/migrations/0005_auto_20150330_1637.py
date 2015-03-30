# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0010_auto_20150330_1637'),
        ('collection_item', '0004_auto_20150330_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='tempitem',
            name='temp_item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='TempItem',
        ),
    ]
