# Generated by Django 5.0.4 on 2024-05-04 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='world',
            name='content',
        ),
        migrations.RemoveField(
            model_name='world',
            name='image',
        ),
    ]