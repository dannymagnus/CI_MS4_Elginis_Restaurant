# Generated by Django 3.2 on 2022-03-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0029_allergen_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=3, max_digits=3)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='allergen',
            name='image',
            field=models.ImageField(blank=True, upload_to='allergens/'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='allergens',
            field=models.ManyToManyField(blank=True, related_name='allergens', to='meals.Allergen'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, upload_to='meals/'),
        ),
    ]
