# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20151015_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='body',
            field=models.CharField(max_length=80, verbose_name='Тело', blank=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='number',
            field=models.CharField(max_length=80, verbose_name='Телефон', blank=True),
        ),
    ]
