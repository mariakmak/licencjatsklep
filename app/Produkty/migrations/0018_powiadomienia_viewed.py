# Generated by Django 4.0.4 on 2022-08-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0017_alter_powiadomienia_konto_alter_powiadomienia_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='powiadomienia',
            name='viewed',
            field=models.BooleanField(null=True),
        ),
    ]
