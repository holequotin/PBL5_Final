# Generated by Django 4.1.7 on 2023-06-08 08:06

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0016_merge_0014_alter_exam_image_0015_exampart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='image',
            field=models.ImageField(default='media/jlpt.jpeg', storage=django.core.files.storage.FileSystemStorage(location='/home/holequoctin/Documents/Nam3_Ki2/PBL5/PBL5/PBL5_Final/PBL5_Final/media'), upload_to='media/'),
        ),
    ]
