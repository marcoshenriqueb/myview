# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-29 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='preço'),
        ),
    ]
