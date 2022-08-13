# Generated by Django 3.2.15 on 2022-08-10 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20220808_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('comment_text',
                 models.TextField()),
                ('published_on',
                 models.DateTimeField(
                     auto_now_add=True)),
                ('star_rating',
                 models.IntegerField(
                     choices=[
                         (1,
                          '⭐'),
                         (2,
                          '⭐⭐'),
                         (3,
                          '⭐⭐⭐'),
                         (4,
                          '⭐⭐⭐⭐'),
                         (5,
                          '⭐⭐⭐⭐⭐')],
                     default=5)),
                ('author',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='commentauthor',
                     to=settings.AUTH_USER_MODEL)),
                ('product',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='reviews',
                     to='products.product')),
            ],
            options={
                'ordering': ['published_on'],
            },
        ),
    ]
