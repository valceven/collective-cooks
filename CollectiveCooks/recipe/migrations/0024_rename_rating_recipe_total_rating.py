# Generated by Django 5.1.2 on 2024-12-01 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0023_delete_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='rating',
            new_name='total_rating',
        ),
    ]
