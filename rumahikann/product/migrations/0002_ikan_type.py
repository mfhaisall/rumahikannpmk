# Generated by Django 5.1.4 on 2024-12-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ikan',
            name='type',
            field=models.CharField(default='emas', max_length=55),
        ),
    ]