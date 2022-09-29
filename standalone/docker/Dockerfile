FROM python:3.7-alpine
LABEL author=dungdl0298@gmail.com

WORKDIR /app

RUN apk update && apk --no-cache add --virtual build-dependencies \
    build-base \
    gcc \
    g++ \
    bash \
    libc-dev \
    libffi-dev \
    openssl-dev \
    libxslt-dev \
    linux-headers \
    openjdk8

COPY Pipfile Pipfile.lock ./
ENV PIPENV_USE_SYSTEM=1

RUN pip install --upgrade pip pipenv && pipenv install --system --deploy

EXPOSE 3101:8080

COPY docker-entrypoint.sh ./
RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
