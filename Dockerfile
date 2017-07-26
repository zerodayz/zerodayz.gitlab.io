FROM alpine:latest

ENV HUGO_VERSION 0.25.1
ENV HUGO_SHA fbf8ca850aaaaad331f5b40bbbe8e797115dab296a8486a53c0561f253ca7b00

# Install HUGO
RUN set -x && \
  apk add --update openssl ca-certificates git && \
  wget -O ${HUGO_VERSION}.tar.gz https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  echo "${HUGO_SHA}  ${HUGO_VERSION}.tar.gz" | sha256sum -c && \
  tar xf ${HUGO_VERSION}.tar.gz && mv hugo* /usr/bin/hugo && \
  rm -r ${HUGO_VERSION}.tar.gz && \
  rm /var/cache/apk/*
