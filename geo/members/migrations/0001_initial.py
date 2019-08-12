# Generated by Django 2.2 on 2019-08-12 14:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=50)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Role')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('employee_number', models.CharField(max_length=7, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$')])),
                ('date_added', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.College')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Role')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
