from django.conf.urls import url, include

urlpatterns = [
    url(r'^pdf_app/', include('pdf_app.urls')),
]
