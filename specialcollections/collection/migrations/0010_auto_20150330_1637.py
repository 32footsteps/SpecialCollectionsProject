# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_collection_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='author',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='item',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]
