# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_embed_videos', '__first__'),
        ('core', '0009_remove_personal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Video', on_delete=django.db.models.deletion.SET_NULL, to='wagtail_embed_videos.EmbedVideo', related_name='+'),
        ),
    ]
