# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def create(apps, schema_editor):
    HomePage = apps.get_model('core.HomePage')
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    HomePage = apps.get_model('core.HomePage')

    # Create content type for homepage model
    homepage_content_type, created = ContentType.objects.get_or_create(
        model='homepage', app_label='home')

    # Create a new homepage
    homepage = HomePage.objects.create(
        title="Homepage",
        slug='home',
        content_type=homepage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=homepage, is_default_site=True)
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151010_2111'),
    ]

    operations = [
        migrations.RunPython(create),
    ]

