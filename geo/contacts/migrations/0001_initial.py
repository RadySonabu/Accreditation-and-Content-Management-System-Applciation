# Generated by Django 3.0.7 on 2020-06-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsRefA01',
            fields=[
                ('ref_a01_rec', models.AutoField(primary_key=True, serialize=False)),
                ('ref_deductions_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('comments', models.TextField()),
                ('active_status', models.BooleanField()),
                ('max_perc', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'db_table': 'accounts_ref_a01',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactContactA00',
            fields=[
                ('contact_a00_rec', models.AutoField(primary_key=True, serialize=False)),
                ('contact_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=50)),
                ('barangay_district', models.CharField(max_length=50)),
                ('city_municipality', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('province', models.CharField(max_length=50)),
                ('phone_1', models.CharField(max_length=31)),
                ('phone_2', models.CharField(max_length=31)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('active_status', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contact_contact_a00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactContactA01',
            fields=[
                ('contact_a01_rec', models.AutoField(primary_key=True, serialize=False)),
                ('skill_id', models.IntegerField()),
                ('comments', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('active_status', models.BooleanField()),
            ],
            options={
                'db_table': 'contact_contact_a01',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactContactA02',
            fields=[
                ('contact_a02_rec', models.AutoField(primary_key=True, serialize=False)),
                ('endorsement_id', models.IntegerField()),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('active_status', models.BooleanField()),
            ],
            options={
                'db_table': 'contact_contact_a02',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactContactA03',
            fields=[
                ('contact_a03_rec', models.AutoField(primary_key=True, serialize=False)),
                ('sample_work_id', models.CharField(max_length=50)),
                ('file_name', models.CharField(max_length=50)),
                ('comments', models.TextField()),
                ('active_status', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contact_contact_a03',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactGroupA00',
            fields=[
                ('group_a00_rec', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('address_1', models.CharField(max_length=50)),
                ('barangay_district', models.CharField(max_length=50)),
                ('city_municipality', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('province', models.CharField(max_length=50)),
                ('phone_1', models.CharField(max_length=31)),
                ('phone_2', models.CharField(max_length=31)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('agent', models.CharField(max_length=50)),
                ('active_status', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contact_group_a00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactGroupA01',
            fields=[
                ('group_a01_rec', models.AutoField(primary_key=True, serialize=False)),
                ('group_role', models.CharField(max_length=50)),
                ('comments', models.TextField()),
                ('active_status', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contact_group_a01',
                'managed': False,
            },
        ),
    ]