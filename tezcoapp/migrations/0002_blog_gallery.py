# Generated by Django 5.0.4 on 2024-05-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tezcoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/blog')),
                ('images', models.ImageField(null=True, upload_to='gallery/blog')),
                ('blogersphoto', models.ImageField(upload_to='gallery/bloguser')),
                ('description', models.CharField(default=None, max_length=200)),
                ('details', models.TextField()),
                ('detailsof', models.TextField()),
                ('name', models.CharField(default=None, max_length=20)),
                ('caption', models.CharField(default=None, max_length=100)),
                ('industry', models.CharField(default=None, max_length=50)),
                ('date', models.DateField(default=None, max_length=20)),
                ('blogersquote', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=40)),
                ('images', models.ImageField(upload_to='gallery/')),
            ],
        ),
    ]
