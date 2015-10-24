# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20151016_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='last_name',
        ),
        migrations.AddField(
            model_name='personal',
            name='fio',
            field=models.CharField(max_length=255, verbose_name='ФИО', blank=True),
        ),
    ]
