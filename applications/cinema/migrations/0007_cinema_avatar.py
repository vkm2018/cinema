# Generated by Django 4.1 on 2022-08-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_preview_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='avatar',
            field=models.ImageField(default=2, upload_to='cinema'),
            preserve_default=False,
        ),
    ]
