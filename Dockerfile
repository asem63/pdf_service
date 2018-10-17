FROM python:2.7

ENV PYTHONUNBUFFERED 1

COPY . /code/
RUN pip install -r /code/config/requirements.txt

WORKDIR /code/

EXPOSE 8000
