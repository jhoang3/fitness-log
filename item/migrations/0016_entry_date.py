# Generated by Django 4.0.3 on 2023-01-09 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_remove_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 9), verbose_name='Publish Date'),
        ),
    ]