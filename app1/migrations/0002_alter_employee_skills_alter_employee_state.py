# Generated by Django 5.1.3 on 2024-12-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Sindh', 'Sindh'), ('Balochistan', 'Balochistan'), ('Islamabad', 'Islamabad'), ('Khyber Pakhtunkhwa', 'Khyber Pakhtunkhwa')], default='Select Province', max_length=200),
        ),
    ]
