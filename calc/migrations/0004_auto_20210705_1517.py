# Generated by Django 3.1.12 on 2021-07-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20210705_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
