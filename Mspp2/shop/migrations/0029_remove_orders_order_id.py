# Generated by Django 4.1.2 on 2022-10-30 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_delete_tracker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_id',
        ),
    ]
