# Generated by Django 2.2 on 2019-08-12 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20190812_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='college',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='role',
        ),
    ]
