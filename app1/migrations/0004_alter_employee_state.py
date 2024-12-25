# Generated by Django 5.1.3 on 2024-12-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_employee_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Sindh', 'Sindh'), ('Balochistan', 'Balochistan'), ('Islamabad', 'Islamabad'), ('Khyber Pakhtunkhwa', 'Khyber Pakhtunkhwa'), ('Gilgit-Baltistan', 'Gilgit-Baltistan'), ('Azad Jammu and Kashmir', 'Azad Jammu and Kashmir'), ('Select Province', 'Select Province')], default='Select Province', max_length=200),
        ),
    ]