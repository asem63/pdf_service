# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import (
    ModelSerializer, IntegerField
)
from pdf_app.models import Url, Document


class UrlSerializer(ModelSerializer):
    document_count = IntegerField(read_only=True)

    class Meta:
        model = Url
        fields = ('id', 'target', 'alive', 'document_count')


class DocumentSerializer(ModelSerializer):
    url_count = IntegerField(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'name', 'url_count')
