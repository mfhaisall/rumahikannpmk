# Generated by Django 5.1.4 on 2024-12-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('gambar', models.CharField(max_length=55)),
                ('harga', models.IntegerField()),
            ],
        ),
    ]
