# Generated by Django 4.0.3 on 2022-11-08 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_entry_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='person',
        ),
    ]
