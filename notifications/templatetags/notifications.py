from django import template
from notifications.models import Notifications


register = template.Library()


@register.inclusion_tag('notifications.html', takes_context=True)
def show_notifications(context):
    user = context['user']
    notifications = Notifications.objects.filter(
        people_to_see__id=user.id)
    if user.is_superuser:
        notifications |= Notifications.objects.filter(need_to_seen_by=1)
    elif user.is_staff:
        notifications |= Notifications.objects.filter(need_to_seen_by=2)
    return {'notifications': notifications}
