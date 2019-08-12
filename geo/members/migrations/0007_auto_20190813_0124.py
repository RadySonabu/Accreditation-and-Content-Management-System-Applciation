# Generated by Django 2.2 on 2019-08-12 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20190812_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(blank=True, max_length=50, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.College')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Role')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Program'),
        ),
    ]
