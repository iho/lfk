# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comment_homepage_personal'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='position',
            field=models.CharField(verbose_name='Должность', blank=True, max_length=255),
        ),
    ]
