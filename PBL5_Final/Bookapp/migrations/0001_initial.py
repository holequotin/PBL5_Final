# Generated by Django 4.2 on 2023-06-08 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Categories')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('summary', models.TextField()),
                ('pdf', models.FileField(upload_to='pdf')),
                ('recommended_books', models.BooleanField(default=False)),
                ('reading_books', models.BooleanField(default=False)),
                ('grammar_books', models.BooleanField(default=False)),
                ('vocabulary_books', models.BooleanField(default=False)),
                ('listen_books', models.BooleanField(default=False)),
                ('tips_books', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(related_name='books', to='Bookapp.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
