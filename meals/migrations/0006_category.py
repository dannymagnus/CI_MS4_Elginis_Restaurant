# Generated by Django 3.2 on 2022-03-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_auto_20220306_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
