# Generated by Django 3.2.15 on 2022-08-08 21:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220807_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dpsodnurd/image/upload/v1652618629/zhtctppqjky78q8h760n.jpg', max_length=255, verbose_name='image'),
        ),
    ]