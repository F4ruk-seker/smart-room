# Generated by Django 4.2.1 on 2023-07-09 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0013_delete_motionsensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='isMaster',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensor',
            name='key',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='keys', to='esp.key'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='usage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='esp',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='esp.esp'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(choices=[('MotionSensor', 'Motion Sensor')], max_length=55),
        ),
    ]
