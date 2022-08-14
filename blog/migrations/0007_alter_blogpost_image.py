# Generated by Django 3.2.15 on 2022-08-14 00:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpostcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dpsodnurd/image/upload/v1660435608/kakhmqytb3vxf0wtywow.png', max_length=255, verbose_name='image'),
        ),
    ]