# Generated by Django 3.2.15 on 2022-08-10 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessage',
            new_name='ArtRequestFormMessage',
        ),
    ]
