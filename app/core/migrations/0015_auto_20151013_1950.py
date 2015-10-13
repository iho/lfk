# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('core', '0014_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='image',
            field=models.ForeignKey(to='wagtailimages.Image', verbose_name='Акция', related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='short_text',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Краткое описание акции', null=True),
        ),
    ]
