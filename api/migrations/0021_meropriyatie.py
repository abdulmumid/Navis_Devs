# Generated by Django 5.2 on 2025-05-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_delete_jobs_alter_about_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meropriyatie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='meropriyatie/')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['id'],
            },
        ),
    ]
