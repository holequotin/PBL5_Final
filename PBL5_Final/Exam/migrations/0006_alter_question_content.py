# Generated by Django 4.1.7 on 2023-05-11 15:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0005_alter_groupquestion_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
