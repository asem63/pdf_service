# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0002_rawpdffile'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawpdffile',
            name='original_name',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
    ]