# Generated by Django 2.2.9 on 2020-01-14 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=10)),
                ('cuil', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('domicilio', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaCorriente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_a_vencer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saldo_vencido', models.DecimalField(decimal_places=2, max_digits=5)),
                ('deuda_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo_cuenta', models.CharField(default='NORMAL', max_length=50)),
                ('estado_cuenta', models.CharField(default='INACTIVO', max_length=50)),
                ('estado_de_mora', models.CharField(default='SIN ATRASO', max_length=50)),
                ('domicilio', models.TextField(max_length=500)),
                ('cliente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
    ]
