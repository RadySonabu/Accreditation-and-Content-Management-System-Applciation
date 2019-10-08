# Generated by Django 2.2 on 2019-10-08 12:15

import django.core.validators
from django.db import migrations, models
import forms.models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0022_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdivisiondetail',
            name='subpoints',
            field=models.DecimalField(db_column='subpoints', decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(forms.models.SubdivisionDetail.max_subpoints)]),
        ),
    ]
