# Generated by Django 3.1.12 on 2021-07-05 14:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calc', '0005_auto_20210705_1522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Score',
            new_name='Adding',
        ),
    ]