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
    first_name = models.CharField("Имя", max_length=255, blank=True)
    last_name = models.CharField("Фамилия", max_length=255, blank=True)
    position = models.CharField("Должность", max_length=255, blank=True)
    # image = ImageField(upload_to="Image")
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
        return self.first_name + " " + self.last_name
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



class RecomendBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    page = PageChooserBlock()
    caption = blocks.RichTextBlock(required=False)
 
    class Meta:
        icon = 'cogs'


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
    class Meta:
        verbose_name = "Пользователь"

# ('image_carousel', blocks.ListBlock(ImageCarouselBlock(),template='yourapp/blocks/carousel.html',icon="image")),
class PersonalIndexPage(Page):
    body = default_body 
    # subpage_types = ['core.Persona']

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
    text = models.TextField("Текст")
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



class License(Page):
    body = StreamField(
            [
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ],

            verbose_name="Тело",
            default=""

            )
    template = "core/licenses.html"
    class Meta:
        verbose_name = "Лицензия"

License.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]

class ServiceIndexPage(Page):
    body = default_body 
    subpage_types = ['core.ServicePage']

    @property
    def services(self):
        services = ServicePage.objects.live().descendant_of(self)
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
    body = default_body 
    # parent_page_types = ['core.ServiceIndexPage']
    parent_page_types = ['core.ServiceIndexPage']

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"



ServicePage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]


class Action(Page):
    active = models.BooleanField("Активная", default=True)
    body = StreamField(
            [
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ],

            verbose_name="Тело",
            default=""

            )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', 
        verbose_name = "Акция"
    )
    short_text = RichTextField('Краткое описание акции', null=True) 
    template = "core/licenses.html"
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

from core.forms import CommentForm
class Comments(Page):

    body = default_body 

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request,  *args, **kwargs)
        comments = Comment.objects.filter(published=True)
        context['comments'] = comments
        return context
    def serve(self, request):
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                inst = form.save()
# send message
                return render(request, self.template, {
                    'self': self,
                })
        else:
            form = self.get_form()

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
