# Generated by Django 4.1 on 2022-08-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_cinema_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='cinema'),
        ),
    ]