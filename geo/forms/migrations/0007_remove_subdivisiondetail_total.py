# Generated by Django 2.2.4 on 2019-08-17 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_remove_subdivisiondetail_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subdivisiondetail',
            name='total',
        ),
    ]