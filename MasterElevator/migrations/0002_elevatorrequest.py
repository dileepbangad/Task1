# Generated by Django 4.2.3 on 2023-07-19 14:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MasterElevator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElevatorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_floor', models.IntegerField()),
                ('request_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('elevator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterElevator.elevator')),
            ],
        ),
    ]
