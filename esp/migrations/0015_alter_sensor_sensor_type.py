# Generated by Django 4.2.1 on 2023-07-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0014_sensor_ismaster_sensor_key_sensor_usage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(choices=[('MotionSensor', 'Motion Sensor'), ('MasterSwitchSensor', 'Master Hand Sensor')], max_length=55),
        ),
    ]
