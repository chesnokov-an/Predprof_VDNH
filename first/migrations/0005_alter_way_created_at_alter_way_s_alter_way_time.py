# Generated by Django 4.1.5 on 2023-02-18 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_way_s_alter_way_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='way',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 2, 18, 10, 57, 23, 297164)),
        ),
        migrations.AlterField(
            model_name='way',
            name='s',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='way',
            name='time',
            field=models.TextField(default=''),
        ),
    ]
