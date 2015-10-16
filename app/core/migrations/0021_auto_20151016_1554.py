# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20151015_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceindexpage',
            name='recomend_block',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('recomend', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), template='core/blocks/recomend_block.html'))), default='', verbose_name='Тело'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='recomend_block',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('recomend', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), template='core/blocks/recomend_block.html'))), default='', verbose_name='Тело'),
        ),
    ]
