# Generated by Django 3.2.8 on 2021-10-22 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransaccionInventario',
            fields=[
                ('idTransaccionInv', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cantidadTransaccion', models.IntegerField()),
                ('valorUnitario', models.FloatField()),
                ('factura', models.CharField(max_length=20)),
                ('tipo', models.CharField(choices=[('C', 'COMPRA'), ('V', 'VENTA'), ('DC', 'DEVOLUCION DE COMPRA'), ('DV', 'DEVOLUCION DE VENTA')], default='I', max_length=2)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
        ),
    ]
