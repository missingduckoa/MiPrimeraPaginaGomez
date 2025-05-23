# Generated by Django 5.2 on 2025-04-20 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptame', '0002_persona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptante',
            name='direccion',
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='adoptante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoptame.adoptante'),
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='fecha_solicitud',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoptame.mascota'),
        ),
    ]
