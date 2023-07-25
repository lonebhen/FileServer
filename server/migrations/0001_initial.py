# Generated by Django 4.2.3 on 2023-07-23 16:16

from django.db import migrations, models
import server.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to=server.models.upload_to('files'))),
                ('number_of_emails', models.PositiveIntegerField(default=0)),
                ('number_of_downloads', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Files',
            },
        ),
    ]
