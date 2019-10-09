from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.blocks import CharBlock, RichTextBlock
from wagtail.core.fields import StreamField


class HomePage(Page):

    body = StreamField([("title", CharBlock()), ("paragraph", RichTextBlock())])

    content_panels = Page.content_panels + [StreamFieldPanel("body")]


class HomePageAfterMigration(Page):

    body = StreamField([("heading", CharBlock()), ("paragraph", RichTextBlock())])

    class Meta:
        db_table = "home_homepage"
        managed = False
