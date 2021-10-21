from django import forms
from core.models import Clase, Grupo, Cuenta, PeriodoContable, TipoTransaccion, Transaccion, Cargo, Empleado, Producto, Entrada
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NuevoUserForm(UserCreationForm):
    
    class Meta: 
        model = User
        fields = ['username', 'password1', 'password2']

        labels = {
            'username':'Usuario ', 
        }

class NuevaClaseForm(forms.ModelForm):
    
    class Meta: 
        model = Clase
        fields = ['codigo','nombre']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Código: '}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
            'codigo':'Código ', 'nombre':'Nombre'
        }

class NuevoGrupoForm(forms.ModelForm):
    class Meta: 
        model = Grupo
        fields = ['codigo','nombre', 'clase']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Último dígito'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'clase': forms.HiddenInput()
        }
        labels = {
            'codigo':'Código ', 'nombre':'Nombre'
        }    
        
class NuevaCuentaForm(forms.ModelForm):
    class Meta: 
        model = Cuenta
        fields = ['codigo','nombre', 'grupo']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Último dígito: '}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'grupo': forms.HiddenInput()
        }
        labels = {
            'codigo':'Código ', 'nombre':'Nombre'
        }  

class NuevoPeriodoForm(forms.ModelForm):
    mes = [('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),('Septiembre','Septiembre'),('Octubre','Octubre'),('Noviembre','Noviembre'),('Diciembre','Diciembre')]
    anio = [('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'),('2026','2026'),('2027','2027'),('2028','2028')]
    
    mes = forms.CharField(widget = forms.Select(choices = mes, attrs={'class':'form-control'}))
    anio = forms.CharField(widget = forms.Select(choices = anio, attrs={'class':'form-control'}))
    class Meta: 
        model = PeriodoContable
        fields = ['mes', 'anio', 'saldoInicial']
        widgets = {
            'mes': forms.Select(attrs={'class':'form-control'}),
            'anio': forms.Select(attrs={'class':'form-control'}),
            'saldoInicial': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Saldo inicial: '})
        }
        labels = {
            'anio':'Año', 'saldoInicial':'Saldo inicial: '
        }
        
class NuevoPeriodoForm2(forms.ModelForm):
    mes = [('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),('Septiembre','Septiembre'),('Octubre','Octubre'),('Noviembre','Noviembre'),('Diciembre','Diciembre')]
    anio = [('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'),('2026','2026'),('2027','2027'),('2028','2028')]
    
    mes = forms.CharField(widget = forms.Select(choices = mes, attrs={'class':'form-control'}))
    anio = forms.CharField(widget = forms.Select(choices = anio, attrs={'class':'form-control'}))
    class Meta: 
        model = PeriodoContable
        fields = ['mes', 'anio']
        widgets = {
            'mes': forms.Select(attrs={'class':'form-control'}),
            'anio': forms.Select(attrs={'class':'form-control'})

        }
        labels = {
            'anio':'Año'
        }
                    
class CuentaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Cuenta):
         return Cuenta.nombre
            
class NuevoTipoTransaccionForm(forms.ModelForm):
    
    cuenta_Debe =  CuentaModelChoiceField(queryset = Cuenta.objects.filter().order_by('codigo'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    cuenta_Haber = CuentaModelChoiceField(queryset = Cuenta.objects.filter().order_by('codigo'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    tipos = [('otro','Otro'),('compra','Compra'),('venta','Venta')]
    
    tipo = forms.CharField(widget = forms.Select(choices = tipos, attrs={'class':'form-control'}))
    class Meta: 
        model = TipoTransaccion
        fields = ['nombre', 'cuenta_Debe', 'cuenta_Haber',  'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'cuenta_Debe': forms.Select(attrs={'class':'form-control'}),
            'cuenta_Haber': forms.Select(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            

        }
        labels = {
            'nombre':'', 'cuentaDebe':'Cuenta Debe', 'tipo':'Tipo de transacción'
        }
        
    def clean_cuenta_Haber(self):
        cuenta_Debe = self.cleaned_data.get("cuenta_Debe")
        cuenta_Haber = self.cleaned_data.get("cuenta_Haber")
            
        if cuenta_Debe == cuenta_Haber:
            raise forms.ValidationError("Por favor seleccione dos cuentas diferentes.")
        return cuenta_Haber
                        
        
class NuevaTransaccionForm(forms.ModelForm):
    class Meta: 
        model = Transaccion
        fields = ['descripcion','monto', 'incluyeIVA', 'periodo', 'tipo']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción: ', 'help-text':'None'}),
            'monto': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Monto: ', 'help-text':'None'}),
            'incluyeIVA': forms.CheckboxInput(),
            'periodo': forms.HiddenInput(),
            'tipo': forms.HiddenInput(),

        }
        labels = {
            'descripcion':'','monto':'', 'incluyeIVA':"Incluye IVA"
        }    
        

class NuevoCargoForm(forms.ModelForm):
    class Meta: 
        model = Cargo
        fields = ['cargo','salario']
        widgets = {
            'cargo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cargo: '}),
            'salario': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Salario base:  '}),
        }
        labels = {
            'cargo':'Cargo', 'salario':'Salario base'
        }
        
class CargoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Cargo):
         return Cargo.cargo

class NuevoEmpleadoForm(forms.ModelForm):
    cargo =  CargoModelChoiceField(queryset = Cargo.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))

    
    class Meta: 
        model = Empleado
        fields = ['dui', 'nombre', 'apellido', 'cargo']
        widgets = {
            'dui': forms.TextInput(attrs={'class':'form-control', 'placeholder':'DUI: '}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'apellido': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido: '}),
            'cargo': forms.Select(attrs={'class':'form-control'}),
            
        }
        labels = {
            'dui':'DUI', 'nombre':'Nombres', 'apellido':'Apellidos', 'cargo':'Cargo'
        }
        
    def clean_nombre(self):
        nombre=self.cleaned_data.get('nombre')
        if nombre.replace(" ","").isalpha():
            return nombre
        else:
            raise forms.ValidationError("Por favor ingrese sus nombres correctamente.")

    def clean_apellido(self):
        apellido=self.cleaned_data.get('apellido')
        if apellido.replace(" ","").isalpha():
            return apellido
        else:
            raise forms.ValidationError("Por favor ingrese sus apellidos correctamente.")
        
    def clean_dui(self):
        dui = self.cleaned_data.get('dui')
        if (dui[1:9].isdigit() and len(dui)==9):
            return dui
        else:
            raise forms.ValidationError('Por favor ingrese el número de DUI sin guiones')

class NuevoProductoForm(forms.ModelForm):
    
    class Meta: 
        model = Producto
        fields = ['nombre','precio', 'unidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio unitario: '}),
            'unidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad de medida: '}),
        }
        labels = {
             'nombre':'Nombre', 'precio':'Precio unitario', 'unidad':'Unidad de medida'
        }

class ProductoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Producto):
         return Producto.nombre
            
class NuevaEntradaForm(forms.ModelForm):
    
    producto =  ProductoModelChoiceField(queryset = Producto.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    

    class Meta: 
        model = Entrada
        fields = ['descripcion', 'producto', 'cantidad']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción: '}),
            'producto': forms.Select(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad: '}),
        }
        labels = {
            'descripcion':'Descripción ', 'producto':'Producto', 'cantidad':'Cantidad '
        }
        
class NuevaSalidaForm(forms.ModelForm):
    
    producto =  ProductoModelChoiceField(queryset = Producto.objects.filter(empty = False).order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    

    class Meta: 
        model = Entrada
        fields = ['descripcion', 'producto', 'cantidad', 'tipo']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción: '}),
            'producto': forms.Select(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad: '}),
            'tipo': forms.HiddenInput()
        }
        labels = {
            'descripcion':'Descripción ', 'producto':'Producto', 'cantidad':'Cantidad '
        }
        