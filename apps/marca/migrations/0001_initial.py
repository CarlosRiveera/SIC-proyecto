# Generated by Django 3.2.8 on 2021-10-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('A', 'ACTIVA'), ('D', 'DESHABILITADA')], default='A', max_length=1)),
            ],
        ),
    ]
