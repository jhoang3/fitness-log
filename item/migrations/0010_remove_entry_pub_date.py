# Generated by Django 4.0.3 on 2022-12-22 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_entry_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='pub_date',
        ),
    ]
