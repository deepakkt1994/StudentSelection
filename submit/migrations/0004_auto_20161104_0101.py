# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-04 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0003_auto_20161104_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='grad_email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='secondary_email',
            field=models.EmailField(max_length=255),
        ),
    ]
