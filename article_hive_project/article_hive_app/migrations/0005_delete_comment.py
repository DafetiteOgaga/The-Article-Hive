# Generated by Django 5.0.7 on 2024-07-14 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_hive_app', '0004_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
