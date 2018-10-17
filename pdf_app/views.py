# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count
from django.db import transaction

from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser

from pdf_app.models import Url, Document
from pdf_app.serializers import (
    UrlSerializer, DocumentSerializer
)
# from pdf_app.tasks import check_urls


class UrlViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_queryset(self):
        queryset = super(UrlViewSet, self).get_queryset()
        queryset = queryset.annotate(document_count=Count('documents'))
        return queryset


class DocumentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = super(DocumentViewSet, self).get_queryset()
        queryset = queryset.annotate(url_count=Count('urls'))
        return queryset

    @action(
        detail=False,
        methods=['post'],
        parser_classes=(MultiPartParser,),
    )
    def upload_file(self, request, pk=None):
        import pdfx
        if 'file' not in request.data:
            raise ParseError("Empty content")
        file = request.data['file']
        path = file.temporary_file_path()
        pdfx_instance = pdfx.PDFx(path)
        urls = pdfx_instance.get_references_as_dict().get('url')
        # here goes with transactions.atomic()
        with transaction.atomic():
            document = Document.objects.create(name=file.name)
            for url in urls:
                record, created = Url.objects.get_or_create(target=url)
                document.urls.add(record)
        return Response('Ok', status=204)
