from django.contrib.sessions.models import Session
from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from wagtail.contrib.modeladmin.options import ModelAdmin
from wagtail.contrib.settings.models import BaseSetting
from wagtail.core.fields import RichTextField


class AbstractCookie(BaseSetting):
    modal_title = models.CharField(
        verbose_name=_('Title'),
        default='We use cookies',
        max_length=255
    )
    modal_text = RichTextField(
        verbose_name=_('Text'),
        default='We use cookies of type X and Y because Z.'
    )
    page_title = models.CharField(
        verbose_name=_('Title'),
        default='Information on cookies',
        max_length=255
    )
    page_introduction = models.TextField(
        verbose_name=_('Introduction'),
        default='This is why we inform u on our use of cookies.'
    )
    page_text = RichTextField(
        verbose_name=_('Text'),
        default='Explanation of our cookies.',
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('modal_title'),
                FieldPanel('modal_text'),
            ],
            heading=_("Modal (popup)"),
        ),
        MultiFieldPanel(
            [
                FieldPanel('page_title'),
                FieldPanel('page_introduction'),
                FieldPanel('page_text'),
            ],
            heading=_("Page"),
        ),
    ]

    class Meta:
        abstract = True
        verbose_name = _("Cookie Wall")


class SessionAdminPermissionHelper(PermissionHelper):
    def user_can_create(self, user):
        return False

    def user_can_edit_obj(self, user, obj):
        return False


class SessionAdmin(ModelAdmin):
    model = Session
    permission_helper_class = SessionAdminPermissionHelper
    list_display = ['session_key', '_hide_modal', '_analytical_cookies', '_third_party_cookies', 'expire_date']
    search_fields = ['session_key']

    def _hide_modal(self, obj):
        return obj.get_decoded().get('hide_modal', False)

    def _analytical_cookies(self, obj):
        return obj.get_decoded().get('analytical_cookies', False)

    def _third_party_cookies(self, obj):
        return obj.get_decoded().get('third_party_cookies', False)
