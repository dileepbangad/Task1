# Generated by Django 4.2.3 on 2023-07-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MasterElevator', '0002_elevatorrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elevatorrequest',
            old_name='elevator_id',
            new_name='elevator',
        ),
    ]
