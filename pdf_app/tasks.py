import os
import urllib3
import pdfx
from celery import shared_task

from django.db import transaction

from pdf_app.models import Url, Document, RawPdfFile


@shared_task
def parse_pdf(raw_pdf_file_id):
    try:
        raw_pdf_file = RawPdfFile.objects.get(id=raw_pdf_file_id)
    except RawPdfFile.DoesNotExists:
        return
    try:
        if os.path.isfile(raw_pdf_file.file.path):
            pdfx_instance = pdfx.PDFx(raw_pdf_file.file.path)
            urls = pdfx_instance.get_references_as_dict().get('url')

            with transaction.atomic():
                document = Document.objects.create(
                    name=raw_pdf_file.original_name
                )
                for url in urls:
                    record, created = Url.objects.get_or_create(target=url)
                    document.urls.add(record)
    finally:
        raw_pdf_file.delete()


@shared_task
def check_url(url_id):
    url = Url.objects.get(id=url_id)
    http = urllib3.PoolManager()
    req = http.request('GET', url.target)
    if req.status == 200:
        url.alive = True
        url.save()
