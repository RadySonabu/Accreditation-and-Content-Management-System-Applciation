# Generated by Django 2.2 on 2019-10-03 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0015_files_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='note',
            new_name='note_from_audited',
        ),
        migrations.AddField(
            model_name='files',
            name='note_from_auditor',
            field=models.TextField(null=True),
        ),
    ]
