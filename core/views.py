from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django import forms
from .forms import NuevaClaseForm, NuevoGrupoForm, NuevaCuentaForm, NuevoPeriodoForm, NuevoPeriodoForm2, NuevoUserForm, NuevoTipoTransaccionForm, NuevaTransaccionForm, NuevoCargoForm
from .forms import NuevoEmpleadoForm, NuevoProductoForm, NuevaEntradaForm, NuevaSalidaForm
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Clase, Grupo, Cuenta, PeriodoContable, CuentaPeriodo, TipoTransaccion, Transaccion, BalanceComprobacion, EstadoResultados, EstadoCapital, BalanceGeneral, Cargo
from .models import Empleado, Planilla, PlanillaGeneral, Producto, Entrada
from django.contrib.auth.models import User
import decimal
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def home2(request, noty):
    n=noty
    return render(request, "core/home.html", {'n':n})

def menu(request,  pk):
    periodo = PeriodoContable.objects.get(id_periodoContable=pk)
    return render(request, "core/filtro.html", {'pk': periodo})


class NuevoUser(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'core/user_form.html'
    form_class = NuevoUserForm
    success_url = reverse_lazy('home2', kwargs = {'noty':6})
    
    def get_form(self, form_class = None):
        form = super(NuevoUser, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario:'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña: '})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar contraseña: '})
        return form

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'core/updateuser.html'
    form_class = NuevoUserForm
    success_url = reverse_lazy('home2', kwargs = {'noty':6})
    
    def get_form(self, form_class = None):
        form = super(UserUpdate, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario:'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña: '})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar contraseña: '})
        return form

def CuentaList(request, noty):
    clases = Clase.objects.all()
    grupos = Grupo.objects.all()
    cuentas = Cuenta.objects.all()
    n = noty
    return render(request, 'core/cuenta_list.html', {'clases': clases, 'grupos': grupos, 'cuentas': cuentas, 'n':n})

def CuentaList2(request, periodo):
    clases = Clase.objects.all()
    grupos = Grupo.objects.all()
    cuentas = Cuenta.objects.all()
    periodo = periodo
    return render(request, 'core/cuenta_list2.html', {'clases': clases, 'grupos': grupos, 'cuentas': cuentas, 'periodo': periodo})
    
class NuevaClase(LoginRequiredMixin, CreateView):
    model = Clase
    form_class = NuevaClaseForm
    success_url = reverse_lazy('core:catalogo', kwargs={'noty':1})
    
class NuevoGrupo(LoginRequiredMixin, CreateView):
    model = Grupo
    form_class = NuevoGrupoForm
    success_url = reverse_lazy('core:catalogo', kwargs={'noty':2})
    
    def get_initial(self):
        initial = super().get_initial()
        initial['clase'] = self.kwargs['clase']
        return initial
    
class NuevaCuenta(LoginRequiredMixin, CreateView):
    model = Cuenta
    form_class = NuevaCuentaForm
    success_url = reverse_lazy('core:catalogo', kwargs={'noty':3})
    
    def get_initial(self):
        initial = super().get_initial()
        initial['grupo'] = self.kwargs['grupo']
        return initial
    
class ClaseList(LoginRequiredMixin, ListView):
    model = Clase
    template_name = 'core/cuentap_list.html'
    
def GrupoList(request):
    clases = Clase.objects.all()
    grupos = Grupo.objects.all()
    return render(request, 'core/cuentah_list.html', {'clases': clases, 'grupos': grupos})
    
class CuentaHijoUpdate(LoginRequiredMixin, UpdateView):
    model = Grupo
    template_name = 'core/cuenta_update.html'
    form_class = NuevoGrupoForm
    success_url = reverse_lazy('core:catalogo', kwargs={'noty':2})

class CuentaNietoUpdate(LoginRequiredMixin, UpdateView):
    model = Cuenta
    template_name = 'core/cuenta_update.html'
    form_class = NuevaCuentaForm
    success_url = reverse_lazy('core:catalogo', kwargs={'noty':3})
    
class CuentaDelete(LoginRequiredMixin, DeleteView):
    model = Cuenta
    template_name= "core/cuenta_delete.html"
    success_url = reverse_lazy('core:catalogo', kwargs={'noty':5})
    
def NuevoPeriodo(request):
    #Contabilidad General. ¡NO TOCAR!
    periodoCant = PeriodoContable.objects.all().count()
    if periodoCant>0:
            ultimoPeriodo = PeriodoContable.objects.latest('id_periodoContable')
            form = NuevoPeriodoForm2(request.POST)
    else:
        form = NuevoPeriodoForm(request.POST)
        
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            
            instancia = PeriodoContable()
            cuentas1 = Cuenta.objects.all()
            periodo = PeriodoContable.objects.latest('id_periodoContable')
                
            for cuenta1 in cuentas1:
                if periodoCant==0:
                    instancia.nuevaCuentaPeriodo(cuenta1, periodo, 0, 0, 0, 0)
                else:
                    saldoCuentaD = CuentaPeriodo.objects.get(cuenta = cuenta1.id, periodo = ultimoPeriodo.id_periodoContable).saldoDeudor
                    saldoCuentaA = CuentaPeriodo.objects.get(cuenta = cuenta1.id, periodo = ultimoPeriodo.id_periodoContable).saldoAcreedor
                    instancia.nuevaCuentaPeriodo(cuenta1, periodo, 0, 0, saldoCuentaD, saldoCuentaA)
                    
            if periodoCant==0:
                Transaccion.objects.create(
                        tipo = TipoTransaccion.objects.get(nombre='Inversión'),
                        periodo = periodo,
                        monto = periodo.saldoInicial,
                        descripcion = 'Inversión Inicial'
                    )
                transaccion = Transaccion.objects.latest('id')
                
                instanciat = Transaccion()
                instanciat.calcularDebeyHaber(transaccion.id)
                
            
            #CONTABILIDAD DE COSTOS
            
            #Lista de empleados
            empleados = Empleado.objects.all()
            
            #Instancia de planilla
            insp = Planilla()
            
            for empleado in empleados:
                #Creal planilla
                Planilla.objects.create(
                    periodo = periodo,
                    empleado = empleado,
                    salarioBase = empleado.cargo.salario
                )
                
                #Obteniendo id
                planilla = Planilla.objects.get(empleado = empleado, periodo = periodo).id
                
                #Realizando calculos
                insp.calcularAFP(planilla)
                insp.calcularISSS(planilla)
                insp.calcularRenta(planilla)
                insp.calcularSalarioNeto(planilla)
                
            
            
            #Crear Planilla General
            PlanillaGeneral.objects.create(
                    periodo = periodo
                )
            
            
            
            #Lista de planillas    
            planillas = Planilla.objects.all()
            
            pg = PlanillaGeneral.objects.get(periodo=periodo)
            for planilla in planillas:
                if planilla.periodo == periodo:
                    pg.AFP = pg.AFP + planilla.AFP
                    pg.ISSS = pg.ISSS + planilla.ISSS
                    pg.renta = pg.renta + planilla.renta
                    pg.salarioNeto = pg.salarioNeto + planilla.salarioNeto
                    pg.salarioBase = pg.salarioBase + planilla.salarioBase
                    pg.comisiones = pg.comisiones + planilla.comisiones
                    pg.ingresos = pg.ingresos + planilla.ingresos
                    pg.retencion = pg.retencion + planilla.retencion
                    pg.save()
                
                
            return redirect('core:periodolist')
    else:
        if periodoCant>0:
            ultimoPeriodo = PeriodoContable.objects.latest('id_periodoContable')
            form = NuevoPeriodoForm2()
        else:
            form = NuevoPeriodoForm()
        
            
    return render(request, 'core/periodo_form.html', {'form':form})

class PeriodoList(LoginRequiredMixin, ListView):
    model = PeriodoContable
    template_name = 'core/periodo_list.html'
    
class PeriodoList2(LoginRequiredMixin, ListView):
    model = PeriodoContable
    template_name = 'core/periodo_list2.html'
    
def NuevoTipoTransaccion(request, periodo):
    p = periodo
    if request.method == 'POST':
        form = NuevoTipoTransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            
            ultimo = TipoTransaccion.objects.latest('id')
            ultimotipo = ultimo.id
            
            instancia = Transaccion()
            instancia.definirCuentaIVA(ultimo.id)
            
            return redirect('core:nuevatransaccion', p, ultimotipo)
    else:
        form = NuevoTipoTransaccionForm()
    
    return render(request, 'core/tipotransaccion_form.html', {'form':form})
    
def TipoTransaccionList(request, pk):
    periodo = pk
    tipotransaccion = TipoTransaccion.objects.all()
    return render(request, 'core/tipotransaccion_list.html', {'periodo': periodo,  'tipotransaccion_list': tipotransaccion})


def TransaccionList(request, pk):
    periodo1 = pk
    transaccion = Transaccion.objects.filter(periodo = periodo1)
    return render(request, 'core/transaccion_list.html', {'periodo': periodo1,  'transaccion_list': transaccion})
    
def NuevaTransaccion(request, tipo, periodo):
    p = periodo
    if request.method == 'POST':
        form = NuevaTransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            
            transaccion = Transaccion.objects.latest('id')
            instancia = Transaccion()
            monto1 = transaccion.monto
            incluye1 = transaccion.incluyeIVA
            
            if transaccion.tipo.tipo == 'otro':
                IVA1 = 0
            else:
                IVA1 = instancia.calcularIVA(monto1, incluye1)

            transaccion.IVA = IVA1
            transaccion.save()
            
            monto2 = instancia.calcularMonto(monto1, incluye1, IVA1)
            transaccion.monto = monto2
            transaccion.save()
            instancia.calcularDebeyHaber(transaccion.id)
            
            
            return redirect('core:detalletransaccion', transaccion.id, 7)
    else:
        form = NuevaTransaccionForm()
        form.initial['tipo'] = tipo
        form.initial['periodo'] = periodo    
    
    return render(request, 'core/transaccion_form.html', {'form':form})


def UpdateTransaccion(request, id):
    transaccion = Transaccion.objects.get(id=id)
    if request.method == 'POST':
        form = NuevaTransaccionForm(request.POST)
        if form.is_valid():
            transaccion.descripcion = form.cleaned_data['descripcion']
            transaccion.monto = form.cleaned_data['monto']
            transaccion.incluyeIVA = form.cleaned_data['incluyeIVA']
            transaccion.save()

            instancia = Transaccion()
            monto1 = transaccion.monto
            incluye1 = transaccion.incluyeIVA
            
            if transaccion.tipo.tipo == 'otro':
                IVA1 = 0
            else:
                IVA1 = instancia.calcularIVA(monto1, incluye1)

            transaccion.IVA = IVA1
            transaccion.save()
            
            monto2 = instancia.calcularMonto(monto1, incluye1, IVA1)
            transaccion.monto = monto2
            transaccion.save()
            instancia.calcularDebeyHaber(transaccion.id)
            
            return redirect('core:detalletransaccion', transaccion.id, 7)
        

    else:
        form = NuevaTransaccionForm()
        form.initial['tipo'] = transaccion.tipo.id
        form.initial['periodo'] = transaccion.periodo.id_periodoContable
        form.initial['descripcion'] = transaccion.descripcion
        form.initial['monto'] = transaccion.monto
        form.initial['incluyeIVA'] = transaccion.incluyeIVA
        return render(request, 'core/transaccion_form.html', {'form':form})


def CerrarPeriodo(request, periodo):
    periodoactual = PeriodoContable.objects.get(id_periodoContable=periodo)
    periodoactual.estadoPeriodo = False
    periodoactual.save()
    
    cuentasp = CuentaPeriodo.objects.all()
    for c in cuentasp:
        if c.periodo.id_periodoContable == periodo:
            if c.saldoDeudor>0:
                c.debe = c.debe + c.saldoDeudor
                c.saldoDeudor=0
            else:
                c.haber = c.haber + c.saldoAcreedor
                c.saldoAcreedor=0
            c.save()
    
    #Crear Balance de Comprobación
    BalanceComprobacion.objects.create(
        periodo = periodoactual
    )
    transaccion_list = Transaccion.objects.all()
    instancia = Transaccion()
    for transaccion in transaccion_list:
        if transaccion.periodo.id_periodoContable == periodo:
            monto1 = transaccion.monto
            incluye1 = transaccion.incluyeIVA
            tipo1 = transaccion.tipo.id
            periodo1 = transaccion.periodo
                
            IVA1 = transaccion.IVA
            
            if transaccion.tipo.tipo != 'otro':
                instancia.asignarIVA(IVA1, tipo1, periodo1)
                    
            monto2 = transaccion.monto

            
            instancia.asignarCpDebe(tipo1, periodo1, monto2, IVA1)
                
            instancia.asignarCpHaber(tipo1, periodo1, monto2, IVA1) 
        
    cuentap_list = CuentaPeriodo.objects.all()
    
    #Calcular balance de comprobación
    bc = BalanceComprobacion.objects.get(periodo = periodo)
    
    for cuentap in cuentap_list:
        if cuentap.periodo.id_periodoContable == periodo:
            cuentap.saldoDeudor = cuentap.saldoDeudor + cuentap.debe - cuentap.haber
            cuentap.saldoAcreedor = cuentap.saldoAcreedor + cuentap.haber - cuentap.debe
            cuentap.save()
            if cuentap.saldoDeudor>0:  
                bc.debe = bc.debe + cuentap.saldoDeudor
            else:
                bc.haber = bc.haber + cuentap.saldoAcreedor
    bc.save()
    
    
    
    
    #Crear Estado de Resultados
    EstadoResultados.objects.create(
        periodo = periodoactual
    )
    
    #Calcular estado de resultados
    er = EstadoResultados.objects.get(periodo=periodo)
    for cuentap in cuentap_list:
        if cuentap.periodo.id_periodoContable == periodo:
            if cuentap.cuenta.grupo.clase.codigo == 4:
                er.utilidades = er.utilidades + cuentap.saldoAcreedor
                er.debe = er.debe + cuentap.saldoAcreedor
                er.save()
            elif cuentap.cuenta.grupo.clase.codigo == 5:
                er.utilidades = er.utilidades - cuentap.saldoDeudor
                er.haber = er.haber + cuentap.saldoDeudor
                er.save()
                
    #Calcular Renta
    instanciaER = EstadoResultados()
    renta = instanciaER.CalcularRenta(er.utilidades, periodo)
    
    #calcular Utilidad Neta
    instanciaER2 = EstadoResultados()
    instanciaER2.calcularUtilidadNeta(er.utilidades, renta, periodo)
    
    #Crear Estado de Capital
    EstadoCapital.objects.create(
        periodo = periodoactual
    )
    
    capital = 0
    for cuentap in cuentap_list:
        if cuentap.periodo.id_periodoContable == periodo and cuentap.cuenta.grupo.clase.codigo == 3:
            capital = capital + cuentap.saldoAcreedor
    
    instanciaEC = EstadoCapital()
    instanciaEC.calcularCapital(capital, periodo)
    
    
    #Crear Balance General
    BalanceGeneral.objects.create(
        periodo = periodoactual
    )
    
    bg = BalanceGeneral.objects.get(periodo = periodo)
    er2 = EstadoResultados.objects.get(periodo=periodo)
    for cuentap in cuentap_list:
        if cuentap.periodo.id_periodoContable == periodo and cuentap.cuenta.grupo.clase.codigo == 1:
           bg.debe = bg.debe + cuentap.saldoDeudor
        elif  cuentap.periodo.id_periodoContable == periodo and cuentap.cuenta.grupo.clase.codigo == 2:
            bg.haber = bg.haber + cuentap.saldoAcreedor
        elif  cuentap.periodo.id_periodoContable == periodo and cuentap.cuenta.grupo.clase.codigo == 3:
            bg.haber = bg.haber + cuentap.saldoAcreedor
    bg.haber = bg.haber + er2.utilidades
    bg.save()
    
    
    return redirect('core:periodolist2')


def ImprimirDetalleTransaccion(request, id, noty):
    tr = Transaccion.objects.get(id = id)
    n = noty
    return render(request, 'core/detalle_transaccion.html', {'tr': tr, 'n':n})

def ImprimirMayorizacion(request, id, periodo):
    periodoant = periodo - int(1)
    cuenta = Cuenta.objects.get(id=id)
    if PeriodoContable.objects.filter(id_periodoContable=periodoant).exists():
        a = PeriodoContable.objects.get(id_periodoContable=periodoant)
        cp3 = CuentaPeriodo.objects.get(cuenta = cuenta, periodo = a).id
        cpa = CuentaPeriodo.objects.get(id = cp3)
        
    periodo2 = PeriodoContable.objects.get(id_periodoContable = periodo)
    cp2 = CuentaPeriodo.objects.get(cuenta = cuenta, periodo = periodo2).id
    
    
    cp = CuentaPeriodo.objects.get(id = cp2)
    
    tr = Transaccion.objects.all()
    if PeriodoContable.objects.filter(id_periodoContable=periodoant).exists():
        return render(request, 'core/mayorizacion.html', {'tr': tr, 'cp':cp, 'cpa': cpa})
    else:
        return render(request, 'core/mayorizacion.html', {'tr': tr, 'cp':cp})

def ImprimirBalanceComprobacion(request, periodo):
    bc = BalanceComprobacion.objects.get(periodo=periodo)
    cp = CuentaPeriodo.objects.all()
    p = PeriodoContable.objects.get(id_periodoContable=periodo)
    return render(request, 'core/balance_comprobacion.html', {'bc': bc, 'cp': cp, 'p': p})

def ImprimirEstadoResultados(request, periodo):
    er = EstadoResultados.objects.get(periodo=periodo)
    cp = CuentaPeriodo.objects.all()
    p = PeriodoContable.objects.get(id_periodoContable=periodo)
    return render(request, 'core/estado_resultados.html', {'er': er, 'cp': cp, 'p': p})

def ImprimirEstadoCapital(request, periodo):
    ec = EstadoCapital.objects.get(periodo=periodo)
    cp = CuentaPeriodo.objects.all()
    p = PeriodoContable.objects.get(id_periodoContable=periodo)
    return render(request, 'core/estado_capital.html', {'ec': ec, 'cp': cp, 'p': p})

def ImprimirBalanceGeneral(request, periodo):
    er = EstadoResultados.objects.get(periodo=periodo)
    bg = BalanceGeneral.objects.get(periodo=periodo)
    cp = CuentaPeriodo.objects.all()
    p = PeriodoContable.objects.get(id_periodoContable=periodo)
    return render(request, 'core/balance_general.html', {'bg': bg, 'cp': cp, 'p': p, 'er': er})

def Informe(request, periodo):
    cp = CuentaPeriodo.objects.all()
    p = PeriodoContable.objects.get(id_periodoContable=periodo)
    i=0
    cps = []
    cantidad = CuentaPeriodo.objects.filter(periodo=periodo).count
    for c in cp:
        cps.append(c.cuenta.nombre)
        i = i + 1
    
    return render(request, 'core/informe.html', {'cp': cp, 'p': p, 'cps':cps, 'cantidad':cantidad})

class BorrarPeriodo(LoginRequiredMixin, DeleteView):
    model = PeriodoContable
    success_url = reverse_lazy('core:periodolist')
    
class BorrarTipo(LoginRequiredMixin, DeleteView):
    model = TipoTransaccion
    success_url = reverse_lazy('home')
    
    
class NuevoCargo(LoginRequiredMixin, CreateView):
    model = Cargo
    form_class = NuevoCargoForm
    success_url = reverse_lazy('core:cargos2')
    
class UpdateCargo(LoginRequiredMixin, UpdateView):
    model = Cargo
    form_class = NuevoCargoForm
    success_url = reverse_lazy('core:cargos2')

class CargoList(LoginRequiredMixin, ListView):
    model = Cargo
    template_name = 'core/cargo_list.html'
    
class CargoList2(LoginRequiredMixin, ListView):
    model = Cargo
    template_name = 'core/cargo_list2.html'
    
class NuevoEmpleado(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = NuevoEmpleadoForm
    success_url = reverse_lazy('core:empleados2')
    
class UpdateEmpleado(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = NuevoEmpleadoForm
    success_url = reverse_lazy('core:empleados2')
    
class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'core/empleado_list.html'
    
class EmpleadoList2(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'core/empleado_list2.html'

def ImprimirPlanillaGeneral(request, periodo):
    pg = PlanillaGeneral.objects.get(periodo=periodo)
    pl = Planilla.objects.all()
    p = periodo
    return render(request, 'core/planilla_general.html', {'pg': pg, 'pl': pl, 'p': p})


class NuevoProducto(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = NuevoProductoForm
    success_url = reverse_lazy('core:productos2')
    
class ProductoList(LoginRequiredMixin, ListView):
    model = Producto
    
class ProductoList2(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'core/producto_list2.html'
    
class UpdateProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = NuevoProductoForm
    success_url = reverse_lazy('core:productos2')
    

def NuevaEntrada(request):
    if request.method == 'POST':
        form = NuevaEntradaForm(request.POST)
        if form.is_valid():
            form.save()
            
            ultima = Entrada.objects.latest('id')
            producto = Producto.objects.get(id = ultima.producto.id)
            
            ultima.total = decimal.Decimal(ultima.cantidad) * ultima.producto.precio
            ultima.C = producto.cantidad + ultima.cantidad
            ultima.T = producto.total + ultima.total
            ultima.save()
            
            producto.cantidad = ultima.cantidad + producto.cantidad
            producto.total = ultima.total + producto.total
            
            if producto.cantidad <= 0:
                producto.empty = True
            else:
                producto.empty = False
                
            producto.save()

            return redirect('core:kardex', 8)
    else:
        form = NuevaEntradaForm()
    
    return render(request, 'core/entrada_form.html', {'form':form})

def NuevaSalida(request):
    if request.method == 'POST':
        form = NuevaSalidaForm(request.POST)
        if form.is_valid():
            form.save()
            
            ultima = Entrada.objects.latest('id')
            producto = Producto.objects.get(id = ultima.producto.id)
            
            ultima.total = decimal.Decimal(ultima.cantidad) * ultima.producto.precio
            ultima.C = producto.cantidad - ultima.cantidad
            ultima.T = producto.total - ultima.total
            ultima.save()
            
            producto.cantidad = producto.cantidad - ultima.cantidad
            producto.total = producto.total - ultima.total
            if producto.cantidad <= 0:
                producto.empty = True
            else:
                producto.empty = False
                
            producto.save()

            return redirect('core:kardex', 9)
    else:
        form = NuevaSalidaForm()
        form.initial['tipo'] = 0
    
    return render(request, 'core/entrada_form.html', {'form':form})

def Kardex(request, noty):
    productos = Producto.objects.all()
    entradas = Entrada.objects.all()
    n = noty
    return render(request, 'core/kardex.html', {'entradas':entradas, 'productos':productos, 'n':n})


def Informe2(request):
    productos = Producto.objects.all()
    i=0
    pc = []
    cantidad = Producto.objects.filter().count
    for p in productos:
        pc.append(p.nombre)
        i = i + 1
    
    return render(request, 'core/informe2.html', {'productos': productos, 'pc':pc, 'cantidad':cantidad})