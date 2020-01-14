from django.db import models
from apps.cliente.models import Cliente

# Create your models here.
class Credito(models.Model):

	cliente = models.ForeignKey(Cliente, null = True, blank = True, on_delete = models.CASCADE)
	capital = models.DecimalField(max_digits=5, decimal_places=2)
	monto_cuota = models.DecimalField(max_digits=5, decimal_places=2)
	vendedor = models.CharField(max_length=50)
	producido = models.DecimalField(max_digits=5, decimal_places=2)
	fecha_inicio = models.DateField()
	estado = models.CharField(max_length=100, default='ACTIVO')
	observacion = models.CharField(max_length=500, default='SIN OBSERVACION')
	inversor = models.CharField(max_length=150, default='SIN INVERSOR')


class Cuota(models.Model):

	credito = models.ForeignKey(Credito, null = True, blank = True, on_delete = models.CASCADE)
	numero_cuota = models.IntegerField()
	monto_cuota = models.DecimalField(max_digits=5, decimal_places=2)
	saldo_cuota = models.DecimalField(max_digits=5, decimal_places=2)	
	fecha_cuota = models.DateField()
	mes_cuota = models.DateField()
	anio_cuota = models.DateField()
	capital = models.DecimalField(max_digits=5, decimal_places=2)
	interes = models.DecimalField(max_digits=5, decimal_places=2)