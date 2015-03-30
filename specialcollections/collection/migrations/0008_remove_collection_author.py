# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_auto_20150330_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='author',
        ),
    ]
