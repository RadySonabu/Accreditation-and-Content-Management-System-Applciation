# Generated by Django 2.2 on 2019-09-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20190901_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='_percent',
            field=models.FloatField(db_column='percent', default=0),
        ),
        migrations.AddField(
            model_name='forms',
            name='_total',
            field=models.FloatField(db_column='total', default=0),
        ),
    ]
