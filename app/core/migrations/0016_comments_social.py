# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0015_auto_20151013_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), verbose_name='Тело', default='')),
            ],
            options={
                'verbose_name': 'Коментарии',
                'verbose_name_plural': 'Коментарии',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('number', wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Телефон')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Тело')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефони',
            },
        ),
    ]
