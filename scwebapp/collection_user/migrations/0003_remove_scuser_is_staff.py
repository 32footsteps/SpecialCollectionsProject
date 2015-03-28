# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_user', '0002_scuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scuser',
            name='is_staff',
        ),
    ]
