# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='selftext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
