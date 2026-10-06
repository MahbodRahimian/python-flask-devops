FROM registry.local:5000/python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY packages/ /app/packages/

RUN pip install \
    --no-cache-dir \
    --no-index \
    --find-links=/app/packages \
    -r /app/requirements.txt

COPY app/ /app/app/
COPY ci_generate_html.py /app/ci_generate_html.py

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "/app/app/main.py"]