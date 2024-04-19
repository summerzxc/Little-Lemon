# Generated by Django 4.1.7 on 2023-02-27 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_booking_reservation_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(choices=[(14, '14:00:00'), (15, '15:00:00'), (16, '16:00:00'), (17, '17:00:00'), (18, '18:00:00'), (19, '19:00:00'), (20, '20:00:00'), (21, '21:00:00'), (22, '22:00:00')], default=22),
        ),
    ]
