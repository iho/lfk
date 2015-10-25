from django.db import models

from wagtail.wagtailcore.models import Page
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext as _
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                MultiFieldPanel,
                                                PageChooserPanel,
                                                StreamFieldPanel)
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtailembeds.blocks import EmbedBlock


from wagtail.wagtailcore.blocks import  RawHTMLBlock

from wagtail.wagtailcore.blocks import PageChooserBlock

from wagtail.wagtailsnippets.blocks import SnippetChooserBlock



from wagtail.wagtailcore.blocks import ListBlock
@register_snippet
class Personal(models.Model):
    fio = models.CharField("ФИО", max_length=255, blank=True)
    text = models.TextField("Текст",  blank=True)
    position = models.CharField("Должность", max_length=255, blank=True)
           
    image = models.ImageField(upload_to="personal_avatars", null=True)
    # image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+', 
    #     verbose_name = "Лицо"
    # )
    # parent_page_types = ['core.PersonalIndexPage']
    # parent_page_types = []
    def __str__(self):
        return self.fio
    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

# Personal.content_panels = [
#     FieldPanel('first_name', classname="full title"),
#     FieldPanel('last_name', classname="full title"),
#     FieldPanel('position', classname="full title"),
#     # StreamFieldPanel('body'),
#     ImageChooserPanel('image'),
#     ]



from wagtail.wagtailcore.blocks import ListBlock
class RecomendBlock(blocks.StructBlock):
    image = ImageChooserBlock("Превью страниц")
    page = PageChooserBlock("Страница")
    short_text = blocks.RichTextBlock("Краткое описания")
 
    class Meta:
        icon = 'cogs'

from django.template.loader import render_to_string

from wagtail.wagtailcore.models import Site
class custom_list_block(blocks.ListBlock): 

    def render(self, value, extra_context=None):
        """
        Return a text rendering of 'value', suitable for display on templates. By default, this will
        use a template if a 'template' property is specified on the block, and fall back on render_basic
        otherwise.
        """
        template = getattr(self.meta, 'template', None)
        class f():
            site = Site.objects.first() 
        if template:
            context = {
                'self': value,
                self.TEMPLATE_VAR: value,
                'request': f() 
            }
            context.update(extra_context or {})
            return render_to_string(template, context)
        else:
            return self.render_basic(value)


recomend_block_default = StreamField(
            [
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('recomend', custom_list_block(RecomendBlock(), template='blocks/recomend_block.html'))
 
    ], 

            verbose_name="Тело",
            default=""

            )




default_body =  StreamField(
            [
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        # ('embedded_video', EmbedBlock(icon="media")),
        ('image', ImageChooserBlock()),
        # ('snippet', SnippetChooserBlock(Personal)),
        # ('raw_html', RawHTMLBlock()),
    ],

            verbose_name="Тело",
            default=""

            )

from wagtail.wagtailcore import blocks
class GoogleMapBlock(blocks.StructBlock):
    map_long = blocks.CharBlock(required=True,max_length=255)
    map_lat = blocks.CharBlock(required=True,max_length=255)
    map_zoom_level = blocks.CharBlock(default=14,required=True,max_length=3)
 
    class Meta:
        template = 'yourapp/blocks/google_map.html'
        icon = 'cogs'
        label = 'Google Map'
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    age = models.IntegerField("Возраст", blank=True, default=0)
    male =  models.BooleanField("Пол", 
            default=True,

choices=[(True, 'Мужчина'), (False, 'Женщина')])
 
    class Meta:
        verbose_name = "Пользователь"

# ('image_carousel', blocks.ListBlock(ImageCarouselBlock(),template='yourapp/blocks/carousel.html',icon="image")),
class PersonalIndexPage(Page):
    body = recomend_block_default
    # subpage_types = ['core.Persona']

    # template = "core/personal.html"
    template = "core/personal.html"
    # @property
    # def services(self):
    #     services = Personal.objects.live().descendant_of(self)
    #     return services

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request,  *args, **kwargs)
        context['personals'] = Personal.objects.all()
        return context 

    class Meta:
        verbose_name = "Заглавная персонала"
        verbose_name_plural = "Заглавные персонала"

PersonalIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]


@register_snippet
class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField("Коментарий")
    published = models.BooleanField("Опубликовать", default=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name = "Отзыв"
        verbose_name = "Отзыв"



from embed_video.fields import EmbedVideoField

from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel
class MenuItem(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        verbose_name=_("Page")
    )
class HomeTopMenuItem(Orderable, MenuItem):
    page = ParentalKey('core.HomePage', related_name='top_menu', verbose_name=_('Page'))

    class Meta:
        verbose_name = _("HomePageServiceItem")
        verbose_name_plural = _('HomePageServiceItems')

class HomeFooterMenuItem(Orderable, MenuItem):
    page = ParentalKey('core.HomePage', related_name='footer_menu', verbose_name=_('Page'))

    class Meta:
        verbose_name = _("HomePageServiceItem")
        verbose_name_plural = _('HomePageServiceItems')




class HomePage(Page):
    video = models.ForeignKey(
        'wagtail_embed_videos.EmbedVideo',
        verbose_name="Video",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = default_body
    personal_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        verbose_name="Страница персонала",
        on_delete=models.SET_NULL, 
        null=True,
        blank=True


    )
    comments_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        verbose_name="Страница отзывов",
        on_delete=models.SET_NULL, 
        null=True,
        blank=True

    )



    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request,  *args, **kwargs)
        action = Action.objects.filter(active=True)[:2]
        if len(action) > 0:
            context['action_0'] = action[0]
        if len(action) > 1:
            context['action_1'] = action[1]
        context['comm'] = Comment.objects.first()
        return context 


    class Meta:
        verbose_name = "Домашняя"
        verbose_name_plural = "Домашняя"

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    InlinePanel('top_menu', label="Верхнее меню"),
    InlinePanel('footer_menu', label="Нижнее меню"),
    PageChooserPanel('personal_page', 'core.PersonalIndexPage'),
    PageChooserPanel('comments_page', 'core.Comments'),
    EmbedVideoChooserPanel('video'),
]

class DefaultPage(Page):
    # body = StreamField(
    #         [
    #     ('heading', blocks.CharBlock(classname="full title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),
    # ],

    #         verbose_name="Тело",
    #         default=""

    #         )
    body = recomend_block_default
    # template = "core/licenses.html"
    template = "core/default.html"
    class Meta:
        verbose_name = "Обычная страница"

DefaultPage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]



class License(Page):
    # body = StreamField(
    #         [
    #     ('heading', blocks.CharBlock(classname="full title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),
    # ],

    #         verbose_name="Тело",
    #         default=""

    #         )
    body = recomend_block_default
    # template = "core/licenses.html"
    template = "core/default.html"
    class Meta:
        verbose_name = "Лицензия"

License.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]

class ServiceIndexPage(Page):
    subpage_types = ['core.ServicePage']
    # second_body = default_body
    body = recomend_block_default
    @property
    def services(self):
        services = ServicePage.objects.all()
        return services

    template = "core/services.html"
    class Meta:
        verbose_name = "Заглавная услуг"
        verbose_name_plural = "Заглавные услуг"

ServiceIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]



class ServicePage(Page):
    body = recomend_block_default
    # parent_page_types = ['core.ServiceIndexPage']
    parent_page_types = ['core.ServiceIndexPage']

    @property
    def services(self):
        services = ServicePage.objects.all()
        return services

    template = "core/services.html"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"



ServicePage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]


class Action(Page):
    active = models.BooleanField("Активная", default=True)
    # body = StreamField(
    #         [
    #     ('heading', blocks.CharBlock(classname="full title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),
    # ],

    #         verbose_name="Тело",
    #         default=""

    #         )
    body = recomend_block_default
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', 
        verbose_name = "Акция"
    )
    short_text = RichTextField('Краткое описание акции', null=True) 
    template = "core/default.html"
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

Action.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('active'),
    FieldPanel('short_text'),
    ImageChooserPanel('image'),
    StreamFieldPanel('body'),
    ]
from django.shortcuts import render

from django.contrib import messages
class Comments(Page):

    body = default_body 

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request,  *args, **kwargs)
        # comments = Comment.objects.filter(published=True)
        # context['comments'] = comments
        return context

    def serve(self, request):
        from core.forms import CommentForm
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                if request.user.is_authenticated():
                    inst = form.save(commit=False)
                    inst.user = request.user
                    inst.save()
                    messages.info(request, 'Сообщенее добавлено.Оно будет доступно для всеобщего обозрения после проверки администратором.')
                else:
                    messages.error(request, 'Коментарии только для авторизированых пользователей.')
# send message
                return render(request, self.template, {
                    'self': self,
                    'form': form,
                })
        else:
            form = CommentForm()

        return render(request, self.template, {
            'self': self,
            'form': form,
        })


    class Meta:
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарии"



Comments.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]



class Social(models.Model):
    number = models.CharField('Телефон', blank=True, 
max_length=80
            )
    body = models.CharField("Тело", blank=True,

max_length=80
            )

    panels = [
        FieldPanel('body'),
        FieldPanel('number'),
    ]

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"



register_snippet(Social)
