# Generated by Django 2.1.7 on 2019-03-28 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190328_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]
