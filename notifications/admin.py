from django.contrib import admin
from notifications.models import Notifications
from notifications.forms import NotificationsFrom
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    form = NotificationsFrom
    list_display = ("get_image", "title", "text")
    readonly_fields = ("seen_by",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request
        return form

    def get_image(self, obj):
        if obj.image:
            return format_html(f"<img src='{obj.image.url}' alt='{obj.title}' class='raya-django-notifications-image'/>")
        else:
            # TODO: Add Default Image Here
            return format_html(f"<img src='' alt='{obj.title}' class='raya-django-notifications-image'/>")

    get_image.short_description = _("Image")

    class Media:
        css = {"all": ("/static/admin/style.css",)}
