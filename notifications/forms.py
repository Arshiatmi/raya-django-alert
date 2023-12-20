from django import forms
from notifications.models import Notifications
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class NotificationsFrom(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"

    def clean(self):
        if self.cleaned_data['need_to_seen_by'] == 3:
            if not self.cleaned_data['people_to_see']:
                raise ValidationError({"people_to_see": _(
                    "This Field Must Be Setted If You Are Choosing Custom User/Users.")})
        else:
            if self.cleaned_data['people_to_see']:
                messages.warning(
                    self.request, _(f"{_('People To See Notifications')} Field Is Ignored Because {_('Need To Seen By')} \
                                     Field Is Not Setted To Custom User/Users."))
                del self.cleaned_data["people_to_see"]
