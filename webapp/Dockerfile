FROM python:3.10-slim as base

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /webapp

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .

FROM base as webapp
ENV PORT=8088
CMD [ "sh", "-c", "gunicorn -b 0.0.0.0:${PORT} api.wsgi:app"]

