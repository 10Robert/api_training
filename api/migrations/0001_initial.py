# Generated by Django 4.2.5 on 2023-09-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=50)),
                ('numero', models.IntegerField(max_length=10)),
                ('habilita', models.BooleanField()),
            ],
        ),
    ]
