# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scuser',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='scuser',
            old_name='last_name',
            new_name='lasname',
        ),
    ]
