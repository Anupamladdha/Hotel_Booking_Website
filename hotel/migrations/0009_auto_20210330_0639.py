# Generated by Django 3.1.7 on 2021-03-30 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20210327_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='order_id',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_id',
            field=models.CharField(default='a', max_length=100),
        ),
    ]
