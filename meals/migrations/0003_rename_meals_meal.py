# Generated by Django 3.2 on 2022-03-01 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_meals_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meals',
            new_name='Meal',
        ),
    ]
