# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin
)
from rest_framework.parsers import MultiPartParser
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from pdf_app.models import Url, Document, RawPdfFile
from pdf_app.serializers import (
    UrlSerializer, DocumentSerializer, RawPdfFileSerializer
)
from pdf_app.filters import UrlFilter, DocumentFilter


class RawPdfFileViewSet(CreateModelMixin, GenericViewSet):
    """
    create:
    Create a new RawPdfFile record, that will be parsed
    (creating new Document and Url records) and then discarded.
    """
    queryset = RawPdfFile.objects.all()
    parser_classes = (MultiPartParser, )
    serializer_class = RawPdfFileSerializer


class UrlViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    retrieve:
    Return the given url.

    list:
    Return a list of all the existing urls.
    """
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    filter_class = UrlFilter
    filter_backends = (
        OrderingFilter,
        DjangoFilterBackend,
    )

    def get_queryset(self):
        queryset = super(UrlViewSet, self).get_queryset()
        queryset = (
            queryset.prefetch_related('documents')
            .annotate(document_count=Count('documents'))
        )
        return queryset


class DocumentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    retrieve:
    Return the given document.

    list:
    Return a list of all the existing documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_class = DocumentFilter
    filter_backends = (
        OrderingFilter,
        DjangoFilterBackend,
    )

    def get_queryset(self):
        queryset = super(DocumentViewSet, self).get_queryset()
        queryset = (
            queryset.prefetch_related('urls')
            .annotate(url_count=Count('urls'))
        )
        return queryset
