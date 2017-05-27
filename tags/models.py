# -*- coding:utf-8 -*-

from django.db import models


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
