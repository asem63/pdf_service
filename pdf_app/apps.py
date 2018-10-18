# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PdfAppConfig(AppConfig):
    name = 'pdf_app'

    def ready(self):
        import pdf_app.receivers  # NOQA: F401
