# Generated by Django 2.2 on 2019-08-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20190812_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='college',
            field=models.CharField(blank=True, default='1', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(blank=True, default='1', max_length=50, null=True),
        ),
    ]
