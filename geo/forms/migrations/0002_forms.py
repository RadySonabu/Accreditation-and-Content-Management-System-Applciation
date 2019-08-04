# Generated by Django 2.2 on 2019-08-03 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('accreditation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.AccreditationType')),
                ('basic_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.BasicInfo')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Division')),
                ('subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Subdivision')),
                ('subdivision_detail', models.ManyToManyField(to='forms.SubdivisionDetail')),
            ],
        ),
    ]
