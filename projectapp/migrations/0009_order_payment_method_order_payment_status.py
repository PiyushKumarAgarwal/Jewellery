# Generated by Django 4.2.4 on 2023-10-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0008_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='COD', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(default=0),
        ),
    ]
