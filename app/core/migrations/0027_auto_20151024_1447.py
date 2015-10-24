# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_personal_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='age',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='male',
        ),
        migrations.AddField(
            model_name='personal',
            name='image',
            field=models.ImageField(null=True, upload_to='personal_avatars'),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='Возраст', blank=True, default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='male',
            field=models.BooleanField(verbose_name='Пол', default=True, choices=[(True, 'Мужчина'), (False, 'Женщина')]),
        ),
    ]
