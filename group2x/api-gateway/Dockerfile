FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt


RUN mkdir -p /src
COPY src/ /src/

EXPOSE 80

WORKDIR /src
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]