# Generated by Django 5.2 on 2025-05-12 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_panel_contactrequest_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactrequest',
            name='phone',
        ),
    ]
