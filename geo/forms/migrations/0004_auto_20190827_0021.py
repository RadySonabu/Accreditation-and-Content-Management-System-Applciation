# Generated by Django 2.2 on 2019-08-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20190822_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]