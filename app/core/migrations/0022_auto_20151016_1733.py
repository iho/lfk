# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20151016_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='recomend_block',
        ),
        migrations.RemoveField(
            model_name='servicepage',
            name='recomend_block',
        ),
        migrations.AlterField(
            model_name='serviceindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('recomend', core.models.custom_list_block(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock('Превью страниц')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock('Страница')), ('short_text', wagtail.wagtailcore.blocks.RichTextBlock('Краткое описания')))), template='blocks/recomend_block.html'))), default='', verbose_name='Тело'),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('recomend', core.models.custom_list_block(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock('Превью страниц')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock('Страница')), ('short_text', wagtail.wagtailcore.blocks.RichTextBlock('Краткое описания')))), template='blocks/recomend_block.html'))), default='', verbose_name='Тело'),
        ),
    ]
