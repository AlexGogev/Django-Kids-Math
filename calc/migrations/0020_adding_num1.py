# Generated by Django 3.1.12 on 2021-07-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0019_auto_20210712_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='adding',
            name='num1',
            field=models.IntegerField(null=True, verbose_name=4),
        ),
    ]
