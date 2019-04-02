# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiseturn', '0006_auto_20190401_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wtuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='wtuser',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='wtuser',
            name='country_of_origin',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='wtuser',
            name='education_level',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='wtuser',
            name='grade',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='wtuser',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='wtuser',
            name='zippostal',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
