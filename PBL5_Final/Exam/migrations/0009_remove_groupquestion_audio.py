# Generated by Django 4.2 on 2023-05-15 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0008_groupquestion_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupquestion',
            name='audio',
        ),
    ]