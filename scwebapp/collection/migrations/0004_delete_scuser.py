# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20150305_0250'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SCUser',
        ),
    ]
