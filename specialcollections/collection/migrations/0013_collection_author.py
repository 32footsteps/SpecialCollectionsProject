# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0012_remove_collection_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None),
            preserve_default=True,
        ),
    ]
