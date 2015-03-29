# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='author',
            field=models.ForeignKey(blank=True, to='collection_user.SCUser'),
            preserve_default=True,
        ),
    ]
