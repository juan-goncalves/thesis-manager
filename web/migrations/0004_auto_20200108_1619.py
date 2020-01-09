# Generated by Django 3.0.2 on 2020-01-08 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_default_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesisstatus',
            name='description',
        ),
        migrations.AddField(
            model_name='thesis',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='web.ThesisStatus'),
        ),
    ]