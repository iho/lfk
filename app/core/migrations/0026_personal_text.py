# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20151024_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]
