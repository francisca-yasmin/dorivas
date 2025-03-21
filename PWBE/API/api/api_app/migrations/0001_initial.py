# Generated by Django 5.1.7 on 2025-03-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('qtdRodas', models.PositiveIntegerField()),
                ('ano', models.PositiveIntegerField()),
                ('cor', models.CharField(max_length=255)),
                ('combustivel', models.CharField(choices=[('Gasolina', 'gasolina'), ('Etanol', 'etanol'), ('GNV', 'gnv'), ('Eletrico', 'eletrico'), ('Acool', 'alcool'), ('Diesel', 'dieses'), ('fb', 'feedback')], max_length=9)),
            ],
        ),
    ]
