# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0016_comments_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='comments_page',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, to='wagtailcore.Page', verbose_name='Страница отзывов'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='personal_page',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, to='wagtailcore.Page', verbose_name='Страница персонала'),
        ),
    ]
