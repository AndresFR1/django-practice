# Generated by Django 5.2.4 on 2025-07-22 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0021_alter_educacion_estudia_actualmente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App1.cargo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='motivo_retiro',
            field=models.CharField(choices=[('voluntario', 'VOLUNTARIO'), ('terminacion_de_contrato', 'TERMINO DE CONTRATO'), ('periodo_de_prueba', 'PERIODO DE PRUEBA'), ('abandono_de_cargo', 'ABANDONO DE CARGO')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tipo_contrato',
            field=models.CharField(choices=[('obra_labor', 'OBRA LABOR'), ('indefinido', 'INDEFINIDO'), ('fijo', 'FIJO'), ('aprendizaje', 'APRENDIZAJE')], default='obra_labor', max_length=20),
        ),
    ]
