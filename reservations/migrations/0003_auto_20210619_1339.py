# Generated by Django 3.2.4 on 2021-06-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_remove_reservation_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='payment_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='trnxid',
            field=models.CharField(max_length=250, null=True),
        ),
    ]