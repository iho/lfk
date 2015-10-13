# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0013_auto_20151013_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Активная')),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), default='', verbose_name='Тело')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
            bases=('wagtailcore.page',),
        ),
    ]
