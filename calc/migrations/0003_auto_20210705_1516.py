# Generated by Django 3.1.12 on 2021-07-05 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20210705_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='numb1',
            new_name='correct',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='numb2',
            new_name='wrong',
        ),
    ]
