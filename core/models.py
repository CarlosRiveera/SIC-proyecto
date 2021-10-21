# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models
import decimal

# Create your models here.


class Clase(models.Model):
	id = models.AutoField(primary_key=True)
	codigo = models.IntegerField('Código', null=False)
	nombre = models.CharField(max_length=256, unique=True)


class Grupo(models.Model):
	id = models.AutoField(primary_key=True)
	clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
	codigo = models.IntegerField('Código', null=False)
	nombre = models.CharField(max_length=256, unique=True)

	class Meta:
		unique_together = ('codigo', 'clase')


class Cuenta(models.Model):
	id = models.AutoField(primary_key=True)
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	codigo = models.IntegerField('Código', null=False)
	nombre = models.CharField(max_length=256, unique=True)

	class Meta:
		unique_together = ('codigo', 'grupo')

	def __str__(self):
		return '{}{}'.format(self.nombre)


class PeriodoContable(models.Model):
	id_periodoContable = models.AutoField(primary_key=True)
	mes = models.TextField(blank=False, null=False)
	anio = models.TextField(blank=False, null=False)
	estadoPeriodo = models.NullBooleanField(default=True)
	saldoInicial = models.DecimalField(max_digits=50, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)], default=0)

	def nuevaCuentaPeriodo(self, argCuenta, argPeriodo, argDebe, argHaber, argSaldo, argSaldoa):
		CuentaPeriodo.objects.create(
			cuenta=argCuenta,
			periodo=argPeriodo,
			debe=argDebe,
			haber=argHaber,
			saldoDeudor=argSaldo,
			saldoAcreedor=argSaldoa
		)


class CuentaPeriodo(models.Model):
	id = models.AutoField(primary_key=True)
	cuenta = models.ForeignKey(Cuenta, blank=True, on_delete=models.CASCADE)
	periodo = models.ForeignKey(
		PeriodoContable, blank=True, on_delete=models.CASCADE)
	debe = models.DecimalField('debe', max_digits=50, decimal_places=2,
							   blank=False, null=False, validators=[MinValueValidator(0)], default=0)
	haber = models.DecimalField('haber', max_digits=50, decimal_places=2,
								blank=False, null=False, validators=[MinValueValidator(0)], default=0)
	saldoDeudor = models.DecimalField(
		max_digits=50, decimal_places=2, blank=False, null=False, default=0.00)
	saldoAcreedor = models.DecimalField(
		max_digits=50, decimal_places=2, blank=False, null=False, default=0.00)


class TipoTransaccion(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=256)
	cuenta_Debe = models.ForeignKey(
		Cuenta, blank=True, on_delete=models.CASCADE, related_name='Cuenta_Debe')
	cuenta_Haber = models.ForeignKey(
		Cuenta, blank=True, on_delete=models.CASCADE, related_name='Cuenta_Haber')
	cuenta_IVA = models.ForeignKey(
		Cuenta, null=True, blank=True, on_delete=models.CASCADE, related_name='Cuenta_IVA')
	tipo = models.CharField(max_length=6, default='otro')


class Transaccion(models.Model):
	id = models.AutoField(primary_key=True)
	tipo = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)
	periodo = models.ForeignKey(PeriodoContable, on_delete=models.CASCADE)
	monto = models.DecimalField(max_digits=20, decimal_places=2,
								blank=False, null=True, validators=[MinValueValidator(0)])
	incluyeIVA = models.BooleanField(default=False)
	IVA = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=True, validators=[
		MinValueValidator(0)], default=False)
	descripcion = models.CharField(max_length=256)
	debe = models.DecimalField(max_digits=20, decimal_places=2,
							   blank=False, default=0, validators=[MinValueValidator(0)])
	haber = models.DecimalField(max_digits=20, decimal_places=2,
								blank=False, default=0, validators=[MinValueValidator(0)])
	fecha = models.DateField(auto_now=True)

	def calcularIVA(self, argMonto, argIncluye):
		factor = decimal.Decimal(0.13)
		divisor = decimal.Decimal(1.13)
		if argIncluye:
			IVA = (argMonto/divisor)*factor
		else:
			IVA = argMonto*factor
		return IVA

	def calcularMonto(self, argMonto, argIncluye, argIVA):
		if argIncluye:
			monto = argMonto
		else:
			monto = argMonto + argIVA
		return monto

	def asignarCpDebe(self, argTipo, argPeriodo, argMonto, argIVA):
		t = TipoTransaccion.objects.get(id=argTipo)

		# Valida si existe
		if CuentaPeriodo.objects.filter(cuenta=t.cuenta_Debe, periodo=argPeriodo).exists():
			cpd = CuentaPeriodo.objects.get(cuenta=t.cuenta_Debe, periodo=argPeriodo)
		else:
			instancia = PeriodoContable()
			instancia.nuevaCuentaPeriodo(t.cuenta_Debe, argPeriodo, 0, 0, 0, 0)
			cpd = CuentaPeriodo.objects.get(cuenta=t.cuenta_Debe, periodo=argPeriodo)

		if t.tipo == 'venta':
			cpd.debe = cpd.debe + argMonto
		else:
			cpd.debe = cpd.debe + (argMonto - argIVA)
		cpd.save()

	def asignarCpHaber(self, argTipo, argPeriodo, argMonto, argIVA):
		t = TipoTransaccion.objects.get(id=argTipo)

		# valida si existe
		if CuentaPeriodo.objects.filter(cuenta=t.cuenta_Haber, periodo=argPeriodo).exists:
			cph = CuentaPeriodo.objects.get(
				cuenta=t.cuenta_Haber, periodo=argPeriodo)
		else:
			instancia = PeriodoContable()
			instancia.nuevaCuentaPeriodo(
				t.cuenta_Haber, argPeriodo, 0, 0, 0, 0)
			cph = CuentaPeriodo.objects.get(
				cuenta=t.cuenta_Haber, periodo=argPeriodo)

		if t.tipo == 'venta':
			cph.haber = cph.haber + (argMonto - argIVA)
		else:
			cph.haber = cph.haber + argMonto
		cph.save()

	def definirCuentaIVA(self, argTipo):
		t = TipoTransaccion.objects.get(id=argTipo)
		if t.tipo == 'venta':
			t.cuenta_IVA = Cuenta.objects.get(nombre='IVA Débito Fiscal')
		elif t.tipo == 'compra':
			t.cuenta_IVA = Cuenta.objects.get(nombre='IVA Crédito Fiscal')
		t.save()

	def asignarIVA(self, argIVA, argTipo, argPeriodo):
		t = TipoTransaccion.objects.get(id=argTipo)
		cuentaIVA = CuentaPeriodo.objects.get(cuenta=t.cuenta_IVA, periodo=argPeriodo)
		if t.tipo == 'venta':
			cuentaIVA.haber = cuentaIVA.haber + argIVA
		else:
			cuentaIVA.debe = cuentaIVA.debe + argIVA
		cuentaIVA.save()

	def __str__(self):
		return '{}{}'.format(self.id)

	def calcularDebeyHaber(self, ID):
		tr = Transaccion.objects.get(id=ID)
		if tr.tipo.tipo == 'venta':
			tr.debe = tr.monto
			tr.haber = tr.monto - tr.IVA
		elif tr.tipo.tipo == 'compra':
			tr.debe = tr.monto-tr.IVA
			tr.haber = tr.monto
		elif tr.tipo.tipo == 'otro':
			tr.debe = tr.monto
			tr.haber = tr.monto
		tr.save()


class BalanceComprobacion(models.Model):
	id = models.AutoField(primary_key=True)
	periodo = models.ForeignKey(
		PeriodoContable, blank=True, on_delete=models.CASCADE)
	debe = models.DecimalField('debe', max_digits=50, decimal_places=2,
							   blank=False, null=True, validators=[MinValueValidator(0)], default=0)
	haber = models.DecimalField('haber', max_digits=50, decimal_places=2,
								blank=False, null=True, validators=[MinValueValidator(0)], default=0)


class EstadoResultados(models.Model):
	id = models.AutoField(primary_key=True)
	periodo = models.ForeignKey(
		PeriodoContable, blank=True, on_delete=models.CASCADE)
	debe = models.DecimalField('debe', max_digits=50, decimal_places=2,
							   blank=False, default=0, validators=[MinValueValidator(0)])
	haber = models.DecimalField('haber', max_digits=50, decimal_places=2,
								blank=False, default=0, validators=[MinValueValidator(0)])
	renta = models.DecimalField(max_digits=50, decimal_places=2,
								blank=False, default=0, validators=[MinValueValidator(0)])
	utilidades = models.DecimalField(
		'Utilildad', max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	utilidadNeta = models.DecimalField(
		'Utilildad', max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])

	def CalcularRenta(self, utilidad, periodo):
		er = EstadoResultados.objects.get(periodo=periodo)
		if utilidad <= decimal.Decimal(472):
			er.renta = decimal.Decimal(0)
		elif utilidad >= decimal.Decimal(472.01) and utilidad <= decimal.Decimal(895.24):
			er.renta = (utilidad - decimal.Decimal(472)) * \
				decimal.Decimal(0.1) + decimal.Decimal(17.67)
		elif utilidad >= decimal.Decimal(895.25) and utilidad <= decimal.Decimal(2038.1):
			er.renta = (utilidad - decimal.Decimal(895.24)) * \
				decimal.Decimal(0.2) + decimal.Decimal(60)
		elif utilidad >= decimal.Decimal(2038.11):
			er.renta = (utilidad - decimal.Decimal(2038.1)) * \
				decimal.Decimal(0.3) + decimal.Decimal(288.57)
		er.save()

		return er.renta

	def calcularUtilidadNeta(self, utilidad, renta, periodo):
		er = EstadoResultados.objects.get(periodo=periodo)
		er.utilidadNeta = utilidad-renta
		er.save()


class EstadoCapital(models.Model):
	id = models.AutoField(primary_key=True)
	periodo = models.ForeignKey(PeriodoContable, on_delete=models.CASCADE)
	capital = models.DecimalField('Capital Contable', max_digits=50, decimal_places=2,
								  blank=False, default=0, validators=[MinValueValidator(0)])

	def calcularCapital(self, argCapital, periodo):
		ec = EstadoCapital.objects.get(periodo=periodo)
		ec.capital = ec.capital + argCapital
		ec.save()


class BalanceGeneral(models.Model):
	id = models.AutoField(primary_key=True)
	periodo = models.ForeignKey(PeriodoContable, on_delete=models.CASCADE)
	debe = models.DecimalField('debe', max_digits=50, decimal_places=2,
							   blank=False, default=0, validators=[MinValueValidator(0)])
	haber = models.DecimalField('haber', max_digits=50, decimal_places=2,
								blank=False, default=0, validators=[MinValueValidator(0)])


class Cargo(models.Model):
	id = models.AutoField(primary_key=True)
	cargo = models.CharField(max_length=256, null=False)
	salario = models.DecimalField(max_digits=50, decimal_places=2, blank=False, null=True, validators=[MinValueValidator(0)])


class Empleado(models.Model):
	id = models.AutoField(primary_key=True)
	dui = models.CharField(unique=True, null=False, max_length=9)
	nombre = models.CharField(max_length=256, null=False)
	apellido = models.CharField(max_length=256, null=False)
	cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '{} {} {} {}'.format(self.dui, self.nombre, self.apellido, self.cargo)


class Planilla(models.Model):
	id = models.AutoField(primary_key=True)
	periodo = models.ForeignKey(PeriodoContable, on_delete=models.CASCADE)
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	AFP = models.DecimalField('AFP', max_digits=50, decimal_places=2,blank=False, default=0, validators=[MinValueValidator(0)])
	ISSS = models.DecimalField('ISSS', max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	renta = models.DecimalField(max_digits=50, decimal_places=2,blank=False, default=0, validators=[MinValueValidator(0)])
	salarioBase = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	comisiones = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	ingresos = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	salarioNeto = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	retencion = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])

	class Meta:
		unique_together = ('periodo', 'empleado')

	def calcularAFP(self, id):
		planilla = Planilla.objects.get(id=id)
		planilla.AFP = (planilla.salarioBase +
						planilla.comisiones) * decimal.Decimal(0.0725)
		planilla.save()

	def calcularISSS(self, id):
		planilla = Planilla.objects.get(id=id)
		planilla.ISSS = (planilla.salarioBase +
						 planilla.comisiones) * decimal.Decimal(0.03)
		planilla.save()

	def calcularRenta(self, id):
		planilla = Planilla.objects.get(id=id)
		sc = planilla.salarioBase + planilla.comisiones
		planilla.ingresos = sc

		if sc <= decimal.Decimal(472):
			planilla.renta = decimal.Decimal(0)

		elif sc >= decimal.Decimal(472.01) and sc <= decimal.Decimal(895.24):
			planilla.renta = (sc - decimal.Decimal(472)) * \
				decimal.Decimal(0.1) + decimal.Decimal(17.67)

		elif sc >= decimal.Decimal(895.25) and sc <= decimal.Decimal(2038.1):
			planilla.renta = (sc - decimal.Decimal(895.24)) * \
				decimal.Decimal(0.2) + decimal.Decimal(60)

		elif sc >= decimal.Decimal(2038.11):
			planilla.renta = (sc - decimal.Decimal(2038.1)) * \
				decimal.Decimal(0.3) + decimal.Decimal(288.57)

		planilla.save()

	def calcularSalarioNeto(self, id):
		planilla = Planilla.objects.get(id=id)

		planilla.salarioNeto = planilla.salarioBase + planilla.comisiones - \
			planilla.AFP - planilla.ISSS - planilla.renta
   
		planilla.retencion = planilla.AFP + planilla.ISSS + planilla.renta

		planilla.save()


class PlanillaGeneral(models.Model):
	id = models.AutoField(primary_key=True)
	periodo = models.ForeignKey(PeriodoContable, on_delete=models.CASCADE)
	AFP = models.DecimalField('AFP', max_digits=50, decimal_places=2,blank=False, default=0, validators=[MinValueValidator(0)])
	ISSS = models.DecimalField('ISSS', max_digits=50, decimal_places=2,blank=False, default=0, validators=[MinValueValidator(0)])
	renta = models.DecimalField(max_digits=50, decimal_places=2,blank=False, default=0, validators=[MinValueValidator(0)])
	salarioBase = models.DecimalField('SalarioTotal', max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	comisiones = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	ingresos = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	salarioNeto = models.DecimalField('Salario Nominal', max_digits=50,decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
	retencion = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
 
 
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=256, null=False)
    precio = models.DecimalField(max_digits=50, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)])
    cantidad = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
    empty = models.BooleanField(default=True)
    unidad = models.CharField(max_length=30, null=False)
    
class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    descripcion = models.CharField(max_length=256)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    total = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
    tipo = models.IntegerField(default=1)
    C = models.IntegerField(default=0)
    T = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
    

