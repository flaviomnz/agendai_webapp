# Generated by Django 5.0.3 on 2024-10-09 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentos.horario')),
            ],
        ),
    ]
