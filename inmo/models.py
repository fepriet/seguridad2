from ast  import Mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
### propiedades
### usuarios 
### negocios

class ComunaPropiedad(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.nombreComuna

class TipoPropiedad(models.Model):
    idTipo = models.AutoField(primary_key=True)
    nombreTipo = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.nombreTipo

class ContratoPropiedad(models.Model):
    idContrato = models.AutoField(primary_key=True)
    nombreContrato = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.nombreContrato

class Propiedad(models.Model):
    propiedad_id = models.AutoField(primary_key=True)
    comuna = models.ForeignKey(ComunaPropiedad,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=500, null = False)
    imagen = models.CharField(max_length=500, null = False)
    imagen2 = models.CharField(max_length=500, null = True, blank = True)
    descripcion = models.CharField(max_length=2500, null = True, blank = True)
    num_dor = models.IntegerField(null = False)
    num_banios = models.IntegerField(null = False)
    num_estac = models.IntegerField(null = False) 
    precio = models.IntegerField(null = False)
    tipo_negocio = models.ForeignKey(TipoPropiedad,on_delete=models.CASCADE)
    disponible = models.BooleanField(null=True)
    owner=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    tipoContrato=models.ForeignKey(ContratoPropiedad,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.direccion

class Compra(models.Model):
    compra_id = models.AutoField(primary_key=True)
    
    propiedad_id = models.CharField(max_length=5, null = False)
    cliente= models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=500, null = False)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo_pago = models.CharField(max_length=500, null = False)
    comentario = models.CharField(max_length=2000, null = False)
    contactado = models.BooleanField(null=True)

    def __str__(self):
        return self.propiedad_id

