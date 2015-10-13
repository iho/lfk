# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0010_homepage_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name_plural': 'Домашняя', 'verbose_name': 'Домашняя'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='personal_page',
            field=models.ForeignKey(to='wagtailcore.Page', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Страница', null=True, related_name='+'),
        ),
    ]
