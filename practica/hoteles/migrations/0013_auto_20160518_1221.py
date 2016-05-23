# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0012_hotel_punt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='punt',
        ),
        migrations.AddField(
            model_name='hotel',
            name='puntuacion',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='body',
            field=models.TextField(default='', max_length=800),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='tipo',
            field=models.CharField(default='', max_length=300),
        ),
    ]
