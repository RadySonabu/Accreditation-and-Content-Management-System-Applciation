# Generated by Django 2.2 on 2019-08-09 06:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('course', models.CharField(choices=[('VPAA', 'Vice President for Academic Affairs'), ('Dean', 'Dean of College'), ('DC', 'Department Chairperson'), ('AD ', 'Administration')], max_length=50)),
                ('college', models.CharField(choices=[('CITE', 'College of Information Technology Education'), ('CEA', 'College of Engineering and Architecture'), ('CBE', 'College of Business Eduction'), ('COA', 'College of Arts'), ('CME', 'College of Maritime Education'), ('N/A', 'Not Applicable')], max_length=50, null=True)),
                ('program', models.CharField(choices=[('BSCS', 'Bachelor of Science in Computer Science'), ('BSIT', 'Bachelor of Science in Information Technology'), ('BSIS', 'Bachelor of Science in Information Systems'), ('BSEMC', 'Bachelor of Science in Entertainment Multimedia Education'), ('BSCE', 'Bachelor of Science in Civil Engineering'), ('BSIE', 'Bachelor of Science in Industrial Engineering'), ('BSChe', 'Bachelor of Science in Chemical Engineering'), ('BSCpe', 'Bachelor of Science in Computer Engineering'), ('BSEE', 'Bachelor of Science in Electrical Engineering'), ('BSECE', 'Bachelor of Science in Electronics and Communications Engineering'), ('BSEnSE', 'Bachelor of Science in Environmental and Sanitary Engineering'), ('BSME', 'Bachelor of Science in Mechanical Engineering'), ('BSIE', 'Bachelor of Science in Industrial Engineering'), ('BSArch', 'Bachelor of Science in Architecture'), ('BSMArE', 'Bachelor of Science in Marine Engineering'), ('BSMT', 'Bachelor of Science in Marine Transportation'), ('BSA', 'Bachelor of Science in Accounting'), ('BSA-LSCM', 'Bachelor of Science in Accounting Major in Logistics and Supply Chain Management'), ('BSA-FMA', 'Bachelor of Science in Accounting Major in financial and Management Accounting'), ('BSA-HRDM', 'Bachelor of Science in Accounting Major in Human Resources Development Management'), ('BSA-MM', 'Bachelor of Science in Accounting Major in Marketing Management'), ('BSA-SMBPO', 'Bachelor of Science in Accounting Major in Service Management for Business Process Outsourcing'), ('BSA-Entrep', 'Bachelor of Science in Accounting in Entrepreneurship'), ('BSA-Act', 'Bachelor of Science in Accounting in Accounting Technology'), ('AB-Engl', 'Bachelor of Arts in English Language'), ('AB-Polsci', 'Bachelor of Arts in Political Science'), ('N/A', 'Not Applicable')], max_length=50, null=True)),
                ('date_added', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
