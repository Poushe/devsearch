# Generated by Django 4.2.1 on 2023-06-27 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Userm',
        ),
    ]