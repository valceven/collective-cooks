# Generated by Django 5.1.1 on 2024-10-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='accounts/default_avatar.png', null=True, upload_to=''),
        ),
    ]
