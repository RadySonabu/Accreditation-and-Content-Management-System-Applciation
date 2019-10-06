# Generated by Django 2.2 on 2019-10-06 05:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0018_auto_20191006_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subdivisiondetail',
            old_name='subpoints',
            new_name='_subpoints',
        ),
        migrations.AlterField(
            model_name='subdivisiondetail',
            name='_subpoints',
            field=models.DecimalField(db_column='subpoints', decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
