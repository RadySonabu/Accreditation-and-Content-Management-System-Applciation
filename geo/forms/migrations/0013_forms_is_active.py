# Generated by Django 2.2 on 2019-10-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_files_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]