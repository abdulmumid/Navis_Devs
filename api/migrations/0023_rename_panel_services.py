# Generated by Django 5.2 on 2025-05-23 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_delete_service'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Panel',
            new_name='Services',
        ),
    ]
