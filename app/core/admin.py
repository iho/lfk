# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, Persona, PersonalIndexPage, Comment, HomePage, License, ServiceIndexPage, ServicePage


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')
admin.site.register(User, UserAdmin)


class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'depth',
        'numchild',
        'title',
        'slug',
        'content_type',
        'live',
        'has_unpublished_changes',
        'url_path',
        'owner',
        'seo_title',
        'show_in_menus',
        'search_description',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
        'sort_order',
        'first_name',
        'last_name',
        'position',
        'image',
    )
    list_filter = (
        'content_type',
        'live',
        'has_unpublished_changes',
        'owner',
        'show_in_menus',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
        'image',
    )
    search_fields = ('slug',)
admin.site.register(Persona, PersonaAdmin)


class PersonalIndexPageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'depth',
        'numchild',
        'title',
        'slug',
        'content_type',
        'live',
        'has_unpublished_changes',
        'url_path',
        'owner',
        'seo_title',
        'show_in_menus',
        'search_description',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
        'body',
    )
    list_filter = (
        'content_type',
        'live',
        'has_unpublished_changes',
        'owner',
        'show_in_menus',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
    )
    search_fields = ('slug',)
admin.site.register(PersonalIndexPage, PersonalIndexPageAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'date')
    list_filter = ('user', 'date')
admin.site.register(Comment, CommentAdmin)


class HomePageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'depth',
        'numchild',
        'title',
        'slug',
        'content_type',
        'live',
        'has_unpublished_changes',
        'url_path',
        'owner',
        'seo_title',
        'show_in_menus',
        'search_description',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
        'body',
    )
    list_filter = (
        'content_type',
        'live',
        'has_unpublished_changes',
        'owner',
        'show_in_menus',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
    )
    search_fields = ('slug',)
admin.site.register(HomePage, HomePageAdmin)


class LicenseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'depth',
        'numchild',
        'title',
        'slug',
        'content_type',
        'live',
        'has_unpublished_changes',
        'url_path',
        'owner',
        'seo_title',
        'show_in_menus',
        'search_description',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
        'body',
    )
    list_filter = (
        'content_type',
        'live',
        'has_unpublished_changes',
        'owner',
        'show_in_menus',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
    )
    search_fields = ('slug',)
admin.site.register(License, LicenseAdmin)


class ServiceIndexPageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'depth',
        'numchild',
        'title',
        'slug',
        'content_type',
        'live',
        'has_unpublished_changes',
        'url_path',
        'owner',
        'seo_title',
        'show_in_menus',
        'search_description',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
        'body',
    )
    list_filter = (
        'content_type',
        'live',
        'has_unpublished_changes',
        'owner',
        'show_in_menus',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
    )
    search_fields = ('slug',)
admin.site.register(ServiceIndexPage, ServiceIndexPageAdmin)


class ServicePageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'depth',
        'numchild',
        'title',
        'slug',
        'content_type',
        'live',
        'has_unpublished_changes',
        'url_path',
        'owner',
        'seo_title',
        'show_in_menus',
        'search_description',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
        'body',
    )
    list_filter = (
        'content_type',
        'live',
        'has_unpublished_changes',
        'owner',
        'show_in_menus',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'first_published_at',
        'latest_revision_created_at',
    )
    search_fields = ('slug',)
admin.site.register(ServicePage, ServicePageAdmin)

