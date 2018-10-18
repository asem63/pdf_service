# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from pdf_app.views import UrlViewSet, DocumentViewSet, RawPdfFileViewSet

router = DefaultRouter()
router.register(r'url', UrlViewSet)
router.register(r'document', DocumentViewSet)
router.register(r'pdf', RawPdfFileViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
