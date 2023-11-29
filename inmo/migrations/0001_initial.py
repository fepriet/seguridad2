# Generated by Django 4.0.5 on 2022-06-21 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComunaPropiedad',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombreComuna', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContratoPropiedad',
            fields=[
                ('idContrato', models.AutoField(primary_key=True, serialize=False)),
                ('nombreContrato', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPropiedad',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombreTipo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('propiedad_id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=500)),
                ('imagen', models.CharField(max_length=500)),
                ('imagen2', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=2500, null=True)),
                ('num_dor', models.IntegerField()),
                ('num_banios', models.IntegerField()),
                ('num_estac', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('disponible', models.BooleanField(null=True)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.comunapropiedad')),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipoContrato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inmo.contratopropiedad')),
                ('tipo_negocio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.tipopropiedad')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('compra_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=500)),
                ('tipo_pago', models.CharField(max_length=500)),
                ('comentario', models.CharField(max_length=2000)),
                ('propiedad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.propiedad')),
            ],
        ),
    ]
