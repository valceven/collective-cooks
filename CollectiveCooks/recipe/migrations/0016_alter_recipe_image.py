# Generated by Django 5.1.1 on 2024-11-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_merge_20241119_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default_food.png', null=True, upload_to=''),
        ),
    ]
