# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.rest_framework import (
    FilterSet,
)

from pdf_app.models import Url, Document

from django.db.models import (
    DateTimeField,
    NullBooleanField,
    BooleanField,
)

from django_filters.rest_framework import (
    BooleanFilter,
)

from django_filters import (
    IsoDateTimeFilter,
)

DEFAULT_FILTER_OVERRIDES = {
    DateTimeField: {
        'filter_class': IsoDateTimeFilter
    },
    BooleanField: {
        'filter_class': BooleanFilter
    },
    NullBooleanField: {
        'filter_class': BooleanFilter
    },
}


class UrlFilter(FilterSet):
    class Meta:
        model = Url
        fields = {
            'target': ['exact', 'icontains'],
            'alive': ['exact'],
            'documents__id': ['in'],
        }
        filter_overrides = DEFAULT_FILTER_OVERRIDES.copy()


class DocumentFilter(FilterSet):
    class Meta:
        model = Document
        fields = {
            'name': ['exact', 'icontains'],
            'urls__id': ['in'],
        }
        filter_overrides = DEFAULT_FILTER_OVERRIDES.copy()
