# Generated by Django 3.2 on 2022-03-19 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0032_alter_drink_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='price',
        ),
    ]