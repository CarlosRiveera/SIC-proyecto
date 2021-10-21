# Generated by Django 2.2.7 on 2019-11-19 23:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191119_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=50, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
