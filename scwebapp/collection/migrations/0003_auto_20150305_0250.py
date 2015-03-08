# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20150305_0249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scuser',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='scuser',
            old_name='lasname',
            new_name='last_name',
        ),
    ]
