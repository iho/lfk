# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0006_auto_20151010_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', parent_link=True, auto_created=True, primary_key=True, serialize=False)),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), verbose_name='Тело', default='')),
            ],
            options={
                'verbose_name': 'Заглавная персонала',
                'verbose_name_plural': 'Заглавные персонала',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name': 'Персонал', 'verbose_name_plural': 'Персонал'},
        ),
    ]
