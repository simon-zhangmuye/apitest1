# Generated by Django 2.1.7 on 2019-03-28 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('admin', '0004_auto_20190328_1936'),
        ('users', '0005_auto_20190328_1942'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='User',
        ),
    ]