# Generated by Django 5.0.2 on 2024-03-01 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_mange', '0002_alter_staff_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_code',
        ),
    ]
