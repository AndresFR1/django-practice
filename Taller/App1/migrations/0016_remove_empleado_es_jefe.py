# Generated by Django 5.2.4 on 2025-07-21 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0015_empleado_es_jefe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='es_jefe',
        ),
    ]
