# Generated by Django 4.0.1 on 2022-01-19 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
