# Generated by Django 4.2.1 on 2023-07-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0016_alter_sensor_sensor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(choices=[('MotionSensor', 'Motion Sensor'), ('MasterSwitchSensor', 'Master Hand Sensor'), ('SilentAlarmSensor', 'Silent Alarm Sensor'), ('AlarmSensor', 'Alarm Sensor')], max_length=55),
        ),
    ]
