# Generated by Django 4.0.4 on 2022-08-13 14:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Produkty', '0008_użytkownik'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Użytkownik',
            new_name='Konto',
        ),
        migrations.AlterModelOptions(
            name='konto',
            options={'verbose_name': 'Konto', 'verbose_name_plural': 'Konta'},
        ),
    ]
