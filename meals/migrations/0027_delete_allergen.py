# Generated by Django 3.2 on 2022-03-09 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0026_remove_meal_allergens'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Allergen',
        ),
    ]
