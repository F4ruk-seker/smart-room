# Generated by Django 4.2 on 2023-04-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0002_alter_esp_esp_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
