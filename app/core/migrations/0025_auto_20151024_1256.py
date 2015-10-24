# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_defaultpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defaultpage',
            options={'verbose_name': 'Обычная страница'},
        ),
        migrations.AddField(
            model_name='personal',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Возраст', blank=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='male',
            field=models.BooleanField(default=True, choices=[(True, 'Мужчина'), (False, 'Женщина')], verbose_name='Пол'),
        ),
    ]
