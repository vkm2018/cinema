# Generated by Django 4.1 on 2022-08-10 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cinema')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cinema.cinema')),
            ],
        ),
    ]