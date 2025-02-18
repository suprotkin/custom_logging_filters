FROM python:3.12-slim-bookworm
LABEL authors="rsuprotkin"

COPY ./requirements.txt /requirements.txt
RUN apt-get update \
  && apt-get install -y \
    build-essential \
    libpcre2-dev \
  && pip install --no-cache-dir uwsgi

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

RUN mkdir -p /opt/app
COPY ./app /opt/app

RUN mkdir -p /configs
COPY ./docker/uwsgi_http.ini /configs/uwsgi_http.ini

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /opt/app

ENTRYPOINT ["/entrypoint.sh"]
