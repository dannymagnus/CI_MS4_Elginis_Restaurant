# Generated by Django 3.2 on 2022-03-20 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.IntegerField()),
                ('postcode', models.CharField(max_length=10)),
                ('street_address', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=500)),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reasons', to='contact.reason')),
            ],
        ),
    ]
