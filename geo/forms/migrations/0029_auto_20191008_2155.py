# Generated by Django 2.2 on 2019-10-08 13:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0028_auto_20191008_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subdivision',
            old_name='points',
            new_name='_points',
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='_points',
            field=models.DecimalField(db_column='points', decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='subdivisiondetail',
            name='subpoints',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
