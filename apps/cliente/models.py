from django.db import models

# Create your models here.
class Cliente(models.Model):

	documento = models.CharField(max_length=10)
	cuil = models.CharField(max_length=15)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	domicilio = models.TextField(max_length=500)
	email = models.EmailField()
	telefono = models.CharField(max_length=20)

class CuentaCorriente(models.Model):

	cliente = models.OneToOneField(Cliente, null = True, blank = True, on_delete = models.CASCADE)
	saldo_a_vencer = models.IntegerField()
	saldo_vencido = models.IntegerField(max_digits=5, decimal_places=2)
	deuda_total = models.IntegerField(max_digits=5, decimal_places=2)
	tipo_cuenta = models.CharField(max_length=50, default='NORMAL')
	estado_cuenta = models.CharField(max_length=50, default='INACTIVO')
	estado_de_mora = models.CharField(max_length=50, default='SIN ATRASO')
	
	
