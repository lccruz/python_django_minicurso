# -*- coding:utf-8 -*-

from django.db import models
from tags.models import Tag


class Noticia(models.Model):
    tags = models.ManyToManyField(Tag)
    id_reddit = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=200,
    )
    url = models.URLField(
        max_length=255
    )
    thumbnail = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )
    created_utc = models.DateTimeField()
    selftext = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
