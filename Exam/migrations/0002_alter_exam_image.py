# Generated by Django 4.1.7 on 2023-04-28 16:36

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='image',
            field=models.ImageField(default='media/jlpt.jpeg', storage=django.core.files.storage.FileSystemStorage(location='/home/holequoctin/Documents/Nam3_Ki2/PBL5/PBL5/PBL5_Final/PBL5_Final/media'), upload_to='media/'),
        ),
    ]
