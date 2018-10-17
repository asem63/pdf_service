import urllib3
from celery import shared_task

from pdf_app.models import Url


@shared_task
def check_urls(url_id):
    url = Url.objects.get(id=url_id)
    http = urllib3.PoolManager()
    req = http.request('GET', url.target)
    if req.status == 200:
        url.alive = True
        url.save()
