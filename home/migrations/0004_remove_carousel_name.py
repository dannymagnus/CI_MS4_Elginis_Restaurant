# Generated by Django 3.2 on 2022-03-21 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_carousel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='name',
        ),
    ]
