# Generated by Django 4.1 on 2022-08-13 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0013_alter_likes_cinema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_cinema', to='cinema.cinema', verbose_name='фильм'),
        ),
    ]