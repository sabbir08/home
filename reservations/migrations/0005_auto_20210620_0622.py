# Generated by Django 3.2.4 on 2021-06-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='father_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='marital_status',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='mother_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='nationality',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='nid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='paymentStatus',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Paid'), ('3', 'Due'), ('4', 'Canceled')], default='Pending', max_length=15),
        ),
        migrations.AddField(
            model_name='reservation',
            name='policeStatus',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Approved'), ('3', 'Canceled')], default='Pending', max_length=15),
        ),
        migrations.AddField(
            model_name='reservation',
            name='trxid',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
