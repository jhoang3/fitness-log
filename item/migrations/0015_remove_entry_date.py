# Generated by Django 4.0.3 on 2023-01-09 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_alter_entry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='date',
        ),
    ]
