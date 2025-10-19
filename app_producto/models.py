from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_categoria = models.IntegerField()
    precio_u = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField(blank=True)
    id_proveedor = models.IntegerField()
