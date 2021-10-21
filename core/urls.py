from django.urls import path
from .views import home, menu, CuentaList, ClaseList, NuevaClase, NuevoGrupo, GrupoList, NuevaCuenta, NuevoPeriodo, PeriodoList, CuentaHijoUpdate, CuentaNietoUpdate, NuevoUser, UserUpdate, NuevoTipoTransaccion, CuentaDelete, TipoTransaccionList, TransaccionList, NuevaTransaccion, CerrarPeriodo, ImprimirBalanceComprobacion, ImprimirEstadoResultados, ImprimirEstadoCapital, ImprimirBalanceGeneral, ImprimirDetalleTransaccion, ImprimirMayorizacion, CuentaList2, BorrarPeriodo
from .views import NuevoCargo, UpdateCargo, CargoList, NuevoEmpleado, UpdateEmpleado, EmpleadoList, ImprimirPlanillaGeneral, UpdateTransaccion, Informe
from .views import NuevoProducto, UpdateProducto, ProductoList, NuevaEntrada, NuevaSalida, Kardex, Informe2, home2, PeriodoList2, CargoList2, EmpleadoList2, ProductoList2
from .views import BorrarTipo

urlpatterns = [
    path('', home, name="home"),
    path('home/<int:noty>', home2, name="home2"),
    path('menu/<int:pk>/', menu, name="menu"),
]

core_patterns = ([
    path('catalogocuentas/<int:noty>', CuentaList, name = 'catalogo'),
    path('catalogocuentasm/<int:periodo>/', CuentaList2, name = 'catalogo2'),
    path('clases/', ClaseList.as_view(), name = 'clases'),
    path('nuevaclase/', NuevaClase.as_view(), name='nuevaclase'),
    path('nuevogrupo/<int:clase>/', NuevoGrupo.as_view(), name='nuevogrupo'),
    path('grupos/', GrupoList, name = 'grupos'),
    path('nuevacuenta/<int:grupo>/', NuevaCuenta.as_view(), name='nuevacuenta'),
    path('nuevoperiodo/', NuevoPeriodo, name='nuevoperiodo'),
    path('periodolist/', PeriodoList.as_view(), name='periodolist'),
    path('periodolist2/', PeriodoList2.as_view(), name='periodolist2'),
    path('subcuentaupdate/<int:pk>/', CuentaHijoUpdate.as_view(), name='updatecuentahijo'),
    path('subsubcuentaupdate/<int:pk>/', CuentaNietoUpdate.as_view(), name='updatecuentanieto'),
    path('nuevousuario/', NuevoUser.as_view(), name='nuevouser'),
    path('usuarioupdate/<int:pk>', UserUpdate.as_view(), name='userupdate'),
    path('nuevotipo/<int:periodo>/', NuevoTipoTransaccion, name='nuevotipo'),
    path('cuentadelete/<int:pk>/', CuentaDelete.as_view(), name='deletecuenta'),
    path('tipos/<int:pk>/', TipoTransaccionList, name='tipos'),
    path('transaccionlist/<int:pk>/', TransaccionList, name='transaccionlist'),
    path('nuevatransaccion/<int:periodo>/<int:tipo>/', NuevaTransaccion, name='nuevatransaccion'),
    path('updatetransaccion/<int:id>/', UpdateTransaccion , name='updatetransaccion'),
    path('cerrarperiodo/<int:periodo>/', CerrarPeriodo, name='cerrarperiodo'),
    path('balancecomprobacion/<int:periodo>/', ImprimirBalanceComprobacion, name='balancecomprobacion'),
    path('estadoresultados/<int:periodo>/', ImprimirEstadoResultados, name='estadoresultados'),
    path('estadocapital/<int:periodo>/', ImprimirEstadoCapital, name='estadocapital'),
    path('balancegeneral/<int:periodo>/', ImprimirBalanceGeneral, name='balancegeneral'),
    path('detalletransaccion/<int:id>/<int:noty>', ImprimirDetalleTransaccion, name='detalletransaccion'),
    path('mayorizacion/<int:id>/<int:periodo>/', ImprimirMayorizacion, name='mayorizacion'),
    path('informe/<int:periodo>/', Informe, name='informe'),
    path('borrar/<int:pk>', BorrarPeriodo.as_view(), name = 'borrar'),
    path('borrartipo/<int:pk>', BorrarTipo.as_view(), name = 'borrartipo'),
    
    
    #Costos
    path('nuevocargo/', NuevoCargo.as_view(), name='nuevocargo'),
    path('updatecargo/<int:pk>', UpdateCargo.as_view(), name='updatecargo'),
    path('cargos/', CargoList.as_view(), name='cargos'),
    path('cargos2/', CargoList2.as_view(), name='cargos2'),
    path('nuevoempleado/', NuevoEmpleado.as_view(), name='nuevoempleado'),
    path('updateempleado/<int:pk>', UpdateEmpleado.as_view(), name='updateempleado'),
    path('empleados/', EmpleadoList.as_view(), name='empleados'),
    path('empleados2/', EmpleadoList2.as_view(), name='empleados2'),
    path('planillageneral/<int:periodo>/', ImprimirPlanillaGeneral, name='planillageneral'),
    path('nuevoproducto/', NuevoProducto.as_view(), name='nuevoproducto'),
    path('updateproducto/<int:pk>', UpdateProducto.as_view(), name='updateproducto'),
    path('productos/', ProductoList.as_view(), name='productos'),
    path('productos2/', ProductoList2.as_view(), name='productos2'),
    path('nuevaentrada/', NuevaEntrada, name='nuevaentrada'),
    path('nuevasalida/', NuevaSalida, name='nuevasalida'),
    path('kardex/<int:noty>', Kardex, name='kardex'),
    path('informe2/', Informe2, name='informe2'),
    

], 'core')