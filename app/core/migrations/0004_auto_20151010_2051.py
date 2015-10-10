# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0003_personal_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, auto_created=True, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), default='', verbose_name='Тело')),
            ],
            options={
                'verbose_name': 'Лицензия',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, auto_created=True, to='wagtailcore.Page')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('first_name', models.CharField(max_length=255, blank=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, blank=True, verbose_name='Фамилия')),
                ('position', models.CharField(max_length=255, blank=True, verbose_name='Должность')),
                ('image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True, verbose_name='Лицо')),
            ],
            options={
                'verbose_name': 'Персонал',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.RemoveField(
            model_name='personal',
            name='image',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Personal',
        ),
    ]
