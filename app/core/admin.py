# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Personal, User, PersonalIndexPage, Comment, MenuItem, HomeTopMenuItem, HomeFooterMenuItem, HomePage, License, ServiceIndexPage, ServicePage, Action, Comments, Social


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'position')
admin.site.register(Personal, PersonalAdmin)


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
    list_display = ('id', 'user', 'text', 'published', 'date')
    list_filter = ('user', 'published', 'date')
admin.site.register(Comment, CommentAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_page')
    list_filter = ('link_page',)
admin.site.register(MenuItem, MenuItemAdmin)


class HomeTopMenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_page', 'sort_order', 'page')
    list_filter = ('link_page', 'page')
admin.site.register(HomeTopMenuItem, HomeTopMenuItemAdmin)


class HomeFooterMenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_page', 'sort_order', 'page')
    list_filter = ('link_page', 'page')
admin.site.register(HomeFooterMenuItem, HomeFooterMenuItemAdmin)


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
        'video',
        'personal_page',
        'comments_page',
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
        'video',
        'personal_page',
        'comments_page',
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


class ActionAdmin(admin.ModelAdmin):
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
        'active',
        'body',
        'image',
        'short_text',
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
        'active',
        'image',
    )
    search_fields = ('slug',)
admin.site.register(Action, ActionAdmin)


class CommentsAdmin(admin.ModelAdmin):
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
admin.site.register(Comments, CommentsAdmin)


class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'body')
admin.site.register(Social, SocialAdmin)

