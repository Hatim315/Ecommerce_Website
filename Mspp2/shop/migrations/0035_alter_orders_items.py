# Generated by Django 4.0.1 on 2022-12-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_alter_orders_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='items',
            field=models.CharField(max_length=550),
        ),
    ]
