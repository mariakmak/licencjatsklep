# Generated by Django 4.0.4 on 2022-08-26 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0021_powiadomienia_produkt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powiadomienia_produkt',
            name='produkt',
        ),
    ]
