# Generated by Django 3.2 on 2024-04-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_userprofile_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='students',
            field=models.JSONField(default=dict),
        ),
    ]
