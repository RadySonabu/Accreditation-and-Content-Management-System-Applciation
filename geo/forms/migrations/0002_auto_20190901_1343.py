# Generated by Django 2.2 on 2019-09-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdivisiondetail',
            name='subpoints',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='subdivisiondetail',
            name='subtotal',
            field=models.FloatField(default=0),
        ),
    ]