# Generated by Django 5.1.2 on 2024-11-25 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0016_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='No Input'),
        ),
    ]
