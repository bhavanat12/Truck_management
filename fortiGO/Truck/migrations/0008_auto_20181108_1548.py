# Generated by Django 2.1.2 on 2018-11-08 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Truck', '0007_auto_20181030_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='route_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='truck_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_id',
        ),
    ]
