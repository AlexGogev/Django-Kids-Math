# Generated by Django 3.1.12 on 2021-07-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0028_auto_20210719_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adding',
            name='num1',
            field=models.IntegerField(blank=True, default=61, null=True),
        ),
    ]
