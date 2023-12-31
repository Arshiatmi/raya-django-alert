# Generated by Django 5.0 on 2023-12-20 17:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='people_to_see',
            field=models.ManyToManyField(blank=True, null=True, related_name='people_to_sees', to=settings.AUTH_USER_MODEL, verbose_name='People To See Notifications'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='need_to_seen_by',
            field=models.IntegerField(choices=[(1, 'Every Superusers'), (2, 'Every Admins'), (3, 'Specific User'), (4, 'Some Multiple Users')], default=4, verbose_name='Need To Seen By'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='seen_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='seen_by', to=settings.AUTH_USER_MODEL, verbose_name='Seen By'),
        ),
    ]
