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
from django.contrib.auth.models import AbstractUser



default_body =  StreamField(
            [
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ],

            verbose_name="Тело",
            default=""

            )


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"


class Persona(Orderable, Page):
    first_name = models.CharField("Имя", max_length=255, blank=True)
    last_name = models.CharField("Фамилия", max_length=255, blank=True)
    position = models.CharField("Должность", max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', 
        verbose_name = "Лицо"
    )
    parent_page_types = ['core.PersonalIndexPage']
    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

Persona.content_panels = [
    FieldPanel('first_name', classname="full title"),
    FieldPanel('last_name', classname="full title"),
    FieldPanel('position', classname="full title"),
    # StreamFieldPanel('body'),
    ImageChooserPanel('image'),
    ]

class PersonalIndexPage(Page):
    body = default_body 
    subpage_types = ['core.Persona']

    @property
    def services(self):
        services = Persona.objects.live().descendant_of(self)
        return services

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
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name = "Отзыв"



class HomePage(Page):
    body = StreamField(
            [
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ],

            verbose_name="Тело",
            default=""

            )
    class Meta:
        verbose_name = "Заглавная"

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
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

    class Meta:
        verbose_name = "Заглавная услуг"
        verbose_name_plural = "Заглавные услуг"

ServiceIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]



class ServicePage(Page):
    body = default_body 
    parent_page_types = ['core.ServiceIndexPage']
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"



ServicePage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    ]


