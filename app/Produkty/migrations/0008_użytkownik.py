# Generated by Django 4.0.4 on 2022-08-13 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Produkty', '0007_alter_oferty_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Użytkownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('data_dolaczenia', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Użytkownik',
                'verbose_name_plural': 'Użytkownicy',
            },
        ),
    ]
