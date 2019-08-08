# Generated by Django 2.2 on 2019-08-08 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccreditationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField(choices=[('ABET', 'American Based Education and Technology'), ('SA', 'Seoul Accord'), ('COE', 'Center of Excellence'), ('COD', 'Center of Development'), ('FP', 'FAAP-PACUCOA'), ('PA', 'PTC-ACBET'), ('PP', 'PCS-PCAB')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(max_length=150)),
                ('points', models.FloatField()),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Division')),
            ],
        ),
        migrations.CreateModel(
            name='SubdivisionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(max_length=150)),
                ('points', models.FloatField()),
                ('subpoints', models.FloatField()),
                ('remarks', models.CharField(max_length=150)),
                ('subtotal', models.FloatField()),
                ('total', models.FloatField()),
                ('subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Subdivision')),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('form_type', models.CharField(choices=[('ABET', 'American Based Education and Technology'), ('SA', 'Seoul Accord'), ('COE', 'Center of Excellence'), ('COD', 'Center of Development'), ('FP', 'FAAP-PACUCOA'), ('PA', 'PTC-ACBET'), ('PP', 'PCS-PCAB')], max_length=100)),
                ('branch', models.CharField(choices=[('MNL', 'Manila Branch'), ('QC', 'Quezon City Branch')], max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('college', models.CharField(choices=[('CITE', 'College of Information Technology Education'), ('CEA', 'College of Engineering and Architecture'), ('CBE', 'College of Business Education'), ('COA', 'College of Arts'), ('CME', 'College of Maritime Education'), ('N/A', 'Not Applicable')], max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(max_length=2)),
                ('last_name', models.CharField(max_length=50)),
                ('division', models.ManyToManyField(blank=True, to='forms.Division')),
            ],
        ),
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('MNL', 'Manila Branch'), ('QC', 'Quezon City Branch')], max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('college', models.CharField(choices=[('CITE', 'College of Information Technology Education'), ('CEA', 'College of Engineering and Architecture'), ('CBE', 'College of Business Education'), ('COA', 'College of Arts'), ('CME', 'College of Maritime Education'), ('N/A', 'Not Applicable')], max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(max_length=2)),
                ('last_name', models.CharField(max_length=50)),
                ('accreditation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.AccreditationType')),
            ],
        ),
    ]
