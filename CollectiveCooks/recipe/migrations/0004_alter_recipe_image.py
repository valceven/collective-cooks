# Generated by Django 5.1.1 on 2024-10-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default_food.png', upload_to=''),
        ),
    ]
