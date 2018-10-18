# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import (
    ModelSerializer, IntegerField
)
from rest_framework.exceptions import ValidationError

from pdf_app.models import Url, Document, RawPdfFile


class UrlSerializer(ModelSerializer):
    document_count = IntegerField(read_only=True)

    class Meta:
        model = Url
        fields = ('id', 'target', 'alive', 'document_count',)


class DocumentSerializer(ModelSerializer):
    url_count = IntegerField(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'name', 'url_count',)
        extra_kwargs = {
            'name': {'required': False},
        }


class RawPdfFileSerializer(ModelSerializer):
    class Meta:
        model = RawPdfFile
        fields = ('file',)
        extra_kwargs = {
            'file': {'required': True},
        }

    def validate(self, data):
        validated_data = super(RawPdfFileSerializer, self).validate(data)
        file_name = data['file'].name
        extension_suffix = file_name.split('.')[-1]
        if extension_suffix != 'pdf':
            raise ValidationError('Bad extension')

        return validated_data

    def create(self, validated_data):
        validated_data['original_name'] = validated_data['file'].name
        return RawPdfFile.objects.create(**validated_data)
