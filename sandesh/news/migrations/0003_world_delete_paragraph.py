# Generated by Django 5.0.4 on 2024-05-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_paragraph_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Paragraph',
        ),
    ]
