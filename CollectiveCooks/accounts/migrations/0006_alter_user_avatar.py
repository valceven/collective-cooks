# Generated by Django 5.1.1 on 2024-10-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default_avatar.png', null=True, upload_to=''),
        ),
    ]