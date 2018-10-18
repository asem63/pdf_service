1. pdfx was selected as url extraction tool for pdf documents because it was 
written specifically for one purpose - extraction of urls from pdf documents.
With pdfx there is no need to manually write regexps, just 1-2 lines of code is
enough to perform url extraction.

2. Django Rest Framework and django-filter were used in this service simply
because they provide quick and painless way to write almost any RESTful web
service.

3. coreapi in pdf_service enables painless api documentation autogeneration.
coreapi library was selected as main api schema generation tool (and
possible microservice interaction tool) because it is part of Django Rest
Framework ecosystem, which means full support for Django Rest Framework and
djano-filter library.

4. nginx + uwsgi was selected beceuse nginx is best production-ready
web server (also contains nice load balancer), as for uwsgi - it is simply
personal preference.

5. pdf parsing and http requests is quite heavy/time consuming tasks
(especially for large pdf files and congested internet connection), threfore
celery (with redis as message broker) was selected as background task host
because it is extreamly easy to integrate it into any django service.

6. reason for Postgres selection as main database is same as with nginx - 
best relational database out there: constant development, good documentation 
and support.
