FROM alpine:latest

ENV HUGO_VERSION 0.26
ENV HUGO_SHA 67e4ba5ec2a02c8164b6846e30a17cc765b0165a5b183d5e480149baf54e1a50

# Install HUGO
RUN set -eux && \
    apk add --update --no-cache \
      ca-certificates \
      openssl && \
  wget -O ${HUGO_VERSION}.tar.gz https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  echo "${HUGO_SHA}  ${HUGO_VERSION}.tar.gz" | sha256sum -c && \
  tar xf ${HUGO_VERSION}.tar.gz && mv hugo* /usr/bin/hugo && \
  rm -r ${HUGO_VERSION}.tar.gz && \
  rm /var/cache/apk/* && \
  hugo version

EXPOSE 1313

CMD ["/usr/local/bin/hugo"]
