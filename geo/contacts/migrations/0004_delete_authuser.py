# Generated by Django 3.0.7 on 2020-06-30 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_authuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
