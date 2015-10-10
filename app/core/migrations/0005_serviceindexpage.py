# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0004_auto_20151010_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), verbose_name='Тело', default='')),
            ],
            options={
                'verbose_name_plural': 'Услуги',
                'verbose_name': 'Услуга',
            },
            bases=('wagtailcore.page',),
        ),
    ]
