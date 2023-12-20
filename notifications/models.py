from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Notifications(models.Model):
    NEED_TO_SEEN_OPTIONS = (
        (1, _("Every Superusers")),
        (2, _("Every Admins")),
        (3, _("Custom User/Users")),
    )
    image = models.ImageField(null=True, blank=True, verbose_name=_("Image"),
                              upload_to="notifications/")
    title = models.CharField(max_length=199, verbose_name=_("Title"))
    text = models.TextField(verbose_name=_("Text"))
    seen_by = models.ManyToManyField(
        get_user_model(), verbose_name=_("Seen By"), related_name="seen_by", null=True, blank=True, editable=False)
    need_to_seen_by = models.IntegerField(default=3,
                                          choices=NEED_TO_SEEN_OPTIONS, verbose_name=_("Need To Seen By"))
    people_to_see = models.ManyToManyField(get_user_model(), verbose_name=_(
        "People To See Notifications"), related_name="people_to_sees", null=True, blank=True,
        help_text="This Field Must Be Setted If You Setted The Field 'Need To Seen By' To 'Custom User/Users'")
    remove_after_seen = models.BooleanField(
        default=True, verbose_name=_("Remove After Seen"))
    notification_format = models.CharField(
        max_length=199, default="{title} : {text}", verbose_name=_("Notification Format To Show In Admin"),
        help_text=_("Available Options Are : image, title, text, seen_by, remove_after_seen"))

    def __str__(self):
        try:
            return self.notification_format.format(
                image=self.image.url if self.image else "",
                title=self.title,
                text=self.text,
                seen_by=','.join((self.seen_by.all())),
                remove_after_seen=str(self.remove_after_seen),
            )
        except KeyError:
            return "<Invalid Notification Format>"

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
