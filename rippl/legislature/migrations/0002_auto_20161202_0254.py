# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='google_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='religion',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='wikipedia_id',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
