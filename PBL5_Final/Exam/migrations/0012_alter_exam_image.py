# Generated by Django 4.2.1 on 2023-06-03 09:02

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0011_alter_exam_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='image',
            field=models.ImageField(default='media/jlpt.jpeg', storage=django.core.files.storage.FileSystemStorage(location='E:\\ki_6\\PBL\\PBL5_Final\\PBL5_Final\\media'), upload_to='media/'),
        ),
    ]