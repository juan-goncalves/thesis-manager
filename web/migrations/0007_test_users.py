# Generated by Django 3.0.2 on 2020-01-10 02:38

from django.db import migrations


# noinspection PyPep8Naming
def populate_test_users(apps, schema_editor):
    User = apps.get_model('web', 'User')
    User(
        username='admin',
        password='pbkdf2_sha256$180000$z3g4HdPhfhvx$LNg+RDfb3zNvdm2xEbyofuemqUyJ1DVXxez4S4S7HJQ=',
        is_superuser=True,
        is_staff=True
    ).save()
    User(
        username='gestor',
        password='pbkdf2_sha256$180000$z3g4HdPhfhvx$LNg+RDfb3zNvdm2xEbyofuemqUyJ1DVXxez4S4S7HJQ=',
        is_manager=True
    ).save()


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0006_remove_thesis_status'),
    ]

    operations = [
        migrations.RunPython(populate_test_users),
    ]