# Generated by Django 3.0.2 on 2020-01-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0004_auto_20200108_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='description',
            field=models.CharField(max_length=1024),
        ),
    ]