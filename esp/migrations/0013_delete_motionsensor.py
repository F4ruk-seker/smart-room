# Generated by Django 4.2.1 on 2023-06-29 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0012_alter_sensor_esp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MotionSensor',
        ),
    ]
