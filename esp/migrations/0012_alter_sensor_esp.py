# Generated by Django 4.2.1 on 2023-06-29 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0011_alter_sensor_sensor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='esp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='esp.esp'),
        ),
    ]
