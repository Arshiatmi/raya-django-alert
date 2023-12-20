from django.test import TestCase
from notifications.models import Notifications


class Setup:
    def SetUp(self):
        Notifications.objects.create(

        )


class NotificationModelTest(Setup, TestCase):
    pass
