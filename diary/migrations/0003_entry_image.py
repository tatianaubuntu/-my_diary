# Generated by Django 4.2 on 2024-10-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_remove_entry_created_at_remove_entry_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение'),
        ),
    ]
