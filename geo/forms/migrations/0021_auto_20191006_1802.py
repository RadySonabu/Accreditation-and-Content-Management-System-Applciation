# Generated by Django 2.2 on 2019-10-06 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0020_auto_20191006_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='subdivisiondetail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forms.SubdivisionDetail'),
        ),
    ]
