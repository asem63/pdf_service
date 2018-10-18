from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

from pdf_service.views import BaseView


urlpatterns = [
    url(r'^$', BaseView.as_view()),
    url(r'^pdf_app/', include('pdf_app.urls')),
    url(r'^docs/', include_docs_urls(title='Pdf service API'))
]
