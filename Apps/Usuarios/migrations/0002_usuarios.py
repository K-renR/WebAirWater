# Generated by Django 3.1.3 on 2024-04-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('rol', models.CharField(max_length=20)),
                ('comunidad', models.CharField(max_length=100)),
            ],
        ),
    ]
