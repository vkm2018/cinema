# Generated by Django 4.1 on 2022-08-12 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_cinema_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preview',
            new_name='Image',
        ),
    ]