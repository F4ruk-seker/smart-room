# Generated by Django 4.2.1 on 2023-06-29 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0009_delete_timeranger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_type', models.CharField(choices=[('MS', 'MotionSensor')], max_length=5)),
                ('esp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esp.esp')),
            ],
        ),
        migrations.CreateModel(
            name='MotionSensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='esp.sensor')),
            ],
            bases=('esp.sensor',),
        ),
    ]
