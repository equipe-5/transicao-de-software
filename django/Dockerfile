FROM python:3.11

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR "/usr/src/app/"
STOPSIGNAL SIGINT

RUN mkdir -p \
        "/usr/src/app/" \
        "/var/www/transition/static/" \
        "/var/www/transition/media/" \
        "/var/run/transition/" \
        "/var/log/transition/" && \
    apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
        ca-certificates build-essential gnupg1 gettext \
        python3-dev libpq-dev postgresql-client libffi-dev \
        libxml2-dev libxmlsec1-dev libxmlsec1-openssl libxslt-dev libssl1.0 && \
    pip install --no-input --no-cache-dir --upgrade \
        pip setuptools wheel && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

ARG MODE
COPY ["./main/requirements/", "./docker/build.sh", "/tmp/transition/"]
RUN sh "/tmp/transition/build.sh" "/tmp/transition/" && \
    rm -rf "/tmp/transition/"

EXPOSE 80

ADD [".", "/usr/src/app/"]
CMD ["/usr/src/app/docker/start.sh"]
