# Generated by Django 5.1.1 on 2024-10-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0002_reporte_gravedad_reporte_urgencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='completado',
            field=models.BooleanField(default=False),
        ),
    ]
