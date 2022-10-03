# Generated by Django 4.0.4 on 2022-08-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0009_rename_użytkownik_konto_alter_konto_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='konto',
            name='data_dolaczenia',
        ),
        migrations.RemoveField(
            model_name='konto',
            name='email',
        ),
        migrations.RemoveField(
            model_name='konto',
            name='imie',
        ),
        migrations.RemoveField(
            model_name='konto',
            name='nazwisko',
        ),
        migrations.AddField(
            model_name='konto',
            name='oferty',
            field=models.ManyToManyField(to='Produkty.oferty'),
        ),
        migrations.AddField(
            model_name='konto',
            name='produkty',
            field=models.ManyToManyField(to='Produkty.produkty'),
        ),
    ]
