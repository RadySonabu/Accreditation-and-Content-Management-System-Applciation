# Generated by Django 2.2 on 2019-08-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_forms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='subdivision_detail',
            field=models.ManyToManyField(related_name='subdivision_detail', to='forms.SubdivisionDetail'),
        ),
    ]
