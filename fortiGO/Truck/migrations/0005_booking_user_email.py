# Generated by Django 2.1.2 on 2018-10-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Truck', '0004_booking_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_email',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]