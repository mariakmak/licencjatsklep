# Generated by Django 4.0.4 on 2022-08-25 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0014_remove_produkty_cena'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nowa_cena', models.DecimalField(decimal_places=2, max_digits=12)),
                ('data_rozpoczecia', models.DateTimeField(auto_now_add=True)),
                ('data_zakonczenia', models.DateTimeField()),
                ('oferta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.oferty')),
            ],
            options={
                'verbose_name': 'Promocja',
                'verbose_name_plural': 'Promocje',
            },
        ),
    ]