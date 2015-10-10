# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings
import django.contrib.auth.models
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import django.utils.timezone
import django.db.models.deletion
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('wagtailimages', '0008_image_created_at_index'),
        ('core', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(unique=True, error_messages={'unique': 'A user with that username already exists.'}, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', max_length=30)),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', related_query_name='user', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', related_query_name='user', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, verbose_name='Имя', max_length=255)),
                ('last_name', models.CharField(blank=True, verbose_name='Фамилия', max_length=255)),
                ('image', models.ForeignKey(related_name='+', verbose_name='Лицо', blank=True, to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
            options={
                'verbose_name': 'Персонал',
            },
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Заглавная'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), verbose_name='Тело', default=''),
        ),
    ]
