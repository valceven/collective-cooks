# Generated by Django 5.1.2 on 2024-11-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_alter_recipe_ingredients_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='No Input'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients_count',
            field=models.IntegerField(default='1'),
        ),
    ]
