# Generated by Django 4.1.7 on 2023-06-07 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0015_practiceparthistory_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practiceparthistory',
            name='user',
        ),
    ]
