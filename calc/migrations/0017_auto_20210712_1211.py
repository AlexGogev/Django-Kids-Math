# Generated by Django 3.1.12 on 2021-07-12 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0016_auto_20210710_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='star',
            old_name='star_count',
            new_name='add',
        ),
    ]