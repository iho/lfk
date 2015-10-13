# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_comment_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.BooleanField(verbose_name='Опубликовать', default=False),
        ),
    ]
