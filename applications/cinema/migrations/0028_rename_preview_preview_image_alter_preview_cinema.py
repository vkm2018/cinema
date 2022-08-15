# Generated by Django 4.1 on 2022-08-15 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0027_rename_image_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preview',
            old_name='preview',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='preview',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cinema.cinema'),
        ),
    ]
