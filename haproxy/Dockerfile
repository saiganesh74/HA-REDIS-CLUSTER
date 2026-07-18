FROM haproxy:3.2

USER root

RUN mkdir -p /var/run && chown -R haproxy:haproxy /var/run

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

USER haproxy