# Generated by Django 4.2.4 on 2023-09-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=10),
        ),
    ]
