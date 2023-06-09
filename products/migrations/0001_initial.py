# Generated by Django 4.1.5 on 2023-05-24 06:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product name')),
                ('price', models.IntegerField(verbose_name='Product price')),
                ('size', models.CharField(max_length=100, verbose_name='Product size')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Product about info')),
                ('poster', models.ImageField(blank=True, upload_to='images/', verbose_name='Products upload image')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posterinfo', to='products.products')),
            ],
        ),
    ]
