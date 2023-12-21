# Generated by Django 5.0 on 2023-12-21 05:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_remove_notifications_specific_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notification_format',
            field=models.CharField(default='{title} : {text}', help_text='Available Options Are : image, title, text, seen_by, remove_after_seen', max_length=199, verbose_name='Notification Format To Show In Admin'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='people_to_see',
            field=models.ManyToManyField(blank=True, help_text="This Field Must Be Setted If You Setted The Field 'Need To Seen By' To 'Custom User/Users'", related_name='people_to_sees', to=settings.AUTH_USER_MODEL, verbose_name='People To See Notifications'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='seen_by',
            field=models.ManyToManyField(blank=True, editable=False, related_name='seen_by', to=settings.AUTH_USER_MODEL, verbose_name='Seen By'),
        ),
    ]
