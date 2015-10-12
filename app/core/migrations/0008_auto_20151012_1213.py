# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('wagtailredirects', '0002_add_verbose_names'),
        ('core', '0007_auto_20151010_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя', blank=True)),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия', blank=True)),
                ('position', models.CharField(max_length=255, verbose_name='Должность', blank=True)),
                ('image', models.ForeignKey(to='wagtailimages.Image', blank=True, verbose_name='Лицо', related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Персонал',
                'verbose_name': 'Персонал',
            },
        ),
        migrations.RemoveField(
            model_name='persona',
            name='image',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='page_ptr',
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Домашняя'},
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
