# Generated by Django 2.1.2 on 2018-10-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Truck', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]