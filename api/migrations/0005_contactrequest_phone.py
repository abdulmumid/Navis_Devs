# Generated by Django 5.2 on 2025-05-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_contactrequest_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='phone',
            field=models.CharField(default='-', max_length=20),
            preserve_default=False,
        ),
    ]
