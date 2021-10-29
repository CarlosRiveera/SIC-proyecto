from django.db import models



# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    existencias = models.IntegerField(default=0)
    stockMinimo= models.IntegerField()
    stockMaximo= models.IntegerField() 
    marca= models.CharField(max_length=20)
    CATEGORIA = (
        ('Zapato para Hombres', 'Zapato para hombres'),
        ('Zapato para Mujeres', 'Zapato para mujeres')
    )
    categoria= models.CharField(max_length=20, choices=CATEGORIA, default='Bolsos para Mujeres')
    ESTADO = (
        ('Activo', 'ACTIVO'),
        ('Deshabilitado', 'DESHABILITADO')
    )
    estado = models.CharField(max_length=15, choices=ESTADO, default='')

    def __str__(self):
        return self.nombre
        


        