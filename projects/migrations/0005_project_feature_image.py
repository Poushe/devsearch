# Generated by Django 4.2.1 on 2023-07-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_user_userm'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='feature_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
