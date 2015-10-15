# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0017_auto_20151015_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeFooterMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(to='core.MenuItem', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('page', modelcluster.fields.ParentalKey(to='core.HomePage', verbose_name='Страница', related_name='footer_menu')),
            ],
            options={
                'verbose_name_plural': 'HomePageServiceItems',
                'verbose_name': 'HomePageServiceItem',
            },
            bases=('core.menuitem', models.Model),
        ),
        migrations.CreateModel(
            name='HomeTopMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(to='core.MenuItem', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('page', modelcluster.fields.ParentalKey(to='core.HomePage', verbose_name='Страница', related_name='top_menu')),
            ],
            options={
                'verbose_name_plural': 'HomePageServiceItems',
                'verbose_name': 'HomePageServiceItem',
            },
            bases=('core.menuitem', models.Model),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', blank=True, null=True, verbose_name='Страница', related_name='+'),
        ),
    ]
