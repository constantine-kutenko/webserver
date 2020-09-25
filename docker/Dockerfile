FROM alpine:3.9

ENV APP_ADDRESS=0.0.0.0 \
    APP_PORT=5000 \
    CONTAINER_USER=nobody \
    CONTAINER_GROUP=nobody

COPY app/0.0.2.py /app/app.py
COPY docker/entrypoint.sh /entrypoint.sh

RUN apk add --no-cache \
        bash \
        python3 \
        curl && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /usr/lib/python*/ensurepip /root/.cache && \
    pip install json2html && \
    chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} /app/ /entrypoint.sh && \
    chmod +x /entrypoint.sh

EXPOSE 5000/tcp

WORKDIR /app

USER ${CONTAINER_USER}:${CONTAINER_GROUP}

ENTRYPOINT ["/entrypoint.sh"]

CMD ["webserver"]
