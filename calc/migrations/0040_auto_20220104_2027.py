# Generated by Django 3.1.12 on 2022-01-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0039_auto_20220104_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adding',
            name='num1',
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
    ]