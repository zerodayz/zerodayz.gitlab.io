FROM alpine:latest

ENV HUGO_VERSION 0.42
ENV HUGO_SHA 788d733a98c6a59ac1584e4ea66ee8329fd66973b7bbfd4835e150175022a2d0

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
