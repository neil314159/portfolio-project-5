# Generated by Django 3.2.15 on 2022-08-12 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_boughtwithitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
    ]