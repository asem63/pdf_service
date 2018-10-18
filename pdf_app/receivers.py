# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from pdf_app.models import RawPdfFile, Url
from pdf_app.tasks import parse_pdf, check_url


@receiver(
    post_save, sender=RawPdfFile, dispatch_uid="raw_pdf_file_parse"
)
def raw_pdf_file_parse(
    sender, instance=None, created=False, **kwargs
):
    if instance and created:
        transaction.on_commit(
            lambda: parse_pdf.delay(instance.id)
        )


@receiver(
    post_delete, sender=RawPdfFile, dispatch_uid="raw_pdf_file_delete"
)
def raw_pdf_file_delete(sender, instance, **kwargs):
    instance.file.delete(False)


@receiver(
    post_save, sender=Url, dispatch_uid="url_check_status"
)
def url_check_status(
    sender, instance=None, created=False, **kwargs
):
    if instance and created:
        transaction.on_commit(
            lambda: check_url.delay(instance.id)
        )
