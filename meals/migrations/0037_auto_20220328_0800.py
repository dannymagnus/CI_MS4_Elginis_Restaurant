# Generated by Django 3.2 on 2022-03-28 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0036_alter_drink_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergen',
            options={'verbose_name': 'Allergen', 'verbose_name_plural': 'Allergens'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='drink',
            options={'verbose_name': 'Drink', 'verbose_name_plural': 'Drinks'},
        ),
        migrations.AlterModelOptions(
            name='drinkcategory',
            options={'verbose_name': 'Drink Category', 'verbose_name_plural': 'Drink Categories'},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'verbose_name': 'Meal', 'verbose_name_plural': 'Meals'},
        ),
    ]
