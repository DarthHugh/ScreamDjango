# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basico', '0002_auto_20160824_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbacklogitem',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='Descrição'),
        ),
    ]