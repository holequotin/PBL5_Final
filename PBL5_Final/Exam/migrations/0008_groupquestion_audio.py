# Generated by Django 4.2 on 2023-05-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0007_alter_exam_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupquestion',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
