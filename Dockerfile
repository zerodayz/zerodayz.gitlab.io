FROM alpine:latest

ENV HUGO_VERSION 0.27.1
ENV HUGO_SHA 0e6cb63e6aca10277b96023c4fed97ac3a3e922d12f073b8a80630946fe289e7

# Install HUGO
RUN set -eux && \
    apk add --update --no-cache \
      ca-certificates \
      openssl \
      git && \
  wget -O ${HUGO_VERSION}.tar.gz https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  echo "${HUGO_SHA}  ${HUGO_VERSION}.tar.gz" | sha256sum -c && \
  tar xf ${HUGO_VERSION}.tar.gz && mv hugo* /usr/bin/hugo && \
  rm -r ${HUGO_VERSION}.tar.gz && \
  rm /var/cache/apk/* && \
  hugo version

EXPOSE 1313

CMD ["/usr/local/bin/hugo"]
