from django.contrib import admin
from apps.cliente.models import Cliente, CuentaCorriente

admin.site.register(Cliente)
admin.site.register(CuentaCorriente)

# Register your models here.
