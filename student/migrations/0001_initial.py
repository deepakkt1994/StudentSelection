# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_first_name', models.CharField(max_length=255)),
                ('primary_last_name', models.CharField(max_length=255)),
                ('optradio', models.CharField(max_length=255)),
            ],
        ),
    ]
