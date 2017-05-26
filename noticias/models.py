# -*- coding:utf-8 -*-

from django.db import models
from tags.models import Tag


class Noticia(models.Model):
    tags = models.ManyToManyField(Tag)
    title = models.CharField(
        max_length=200,
    )
    url = models.URLField()
    thumbnail = models.URLField(
        blank=True,
        null=True,
    )
    created_utc = models.DateTimeField()
    selftext = models.TextField(
        blank=True,
        null=True,
    )
