# Generated by Django 4.1.7 on 2023-02-26 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('menu_item_description', models.TextField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('reservation_date', models.DateField(default=django.utils.timezone.now)),
                ('reservation_slot', models.SmallIntegerField(default=10)),
            ],
            options={
                'unique_together': {('reservation_date', 'reservation_slot')},
            },
        ),
    ]
