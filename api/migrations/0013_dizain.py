# Generated by Django 5.2 on 2025-05-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_consult_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dizain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='dizain/')),
            ],
        ),
    ]
