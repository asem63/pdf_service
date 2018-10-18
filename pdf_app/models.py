# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Url(models.Model):
    """
    Category information
    """
    target = models.URLField(max_length=4096, blank=True, null=True)
    alive = models.NullBooleanField(default=False)


class Document(models.Model):
    """
    App information
    """
    name = models.CharField(max_length=4096, blank=True, null=True)
    urls = models.ManyToManyField(Url, related_name='documents')


class RawPdfFile(models.Model):
    original_name = models.CharField(max_length=4096, blank=True, null=True)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
