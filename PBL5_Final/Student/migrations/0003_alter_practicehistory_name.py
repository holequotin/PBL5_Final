# Generated by Django 4.1.7 on 2023-05-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_practicehistory_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicehistory',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]