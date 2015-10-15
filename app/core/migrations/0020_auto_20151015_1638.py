# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20151015_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
    ]
