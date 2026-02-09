FROM sennet/data-products-ui-base:latest

RUN apt-get update \
 && apt-get -y install \
    uwsgi \
    uwsgi-plugin-python3 \
 && rm -rf /var/cache/apt/*

COPY sennet /opt/integrated-maps-ui
COPY uwsgi /opt/uwsgi

WORKDIR /opt/integrated-maps-ui
RUN mv integrated_maps_ui/production_settings.py integrated_maps_ui/local_settings.py
RUN python3 -m compileall .
RUN python3 -O -m compileall .

ENV DJANGO_SETTINGS_MODULE integrated_maps_ui.settings

VOLUME /opt/secret

EXPOSE 5000

ENTRYPOINT ["uwsgi",  "--plugin", "python3", "-H", "/opt/venv", "--xml", "/opt/uwsgi/uwsgi.xml"]
