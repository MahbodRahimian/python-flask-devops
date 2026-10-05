FROM python:3.12-slim

WORKDIR /app

COPY app/ /app/app/

COPY ci_generate_html.py /app/ci_generate_html.py

RUN pip install --no-cache-dir flask requests

EXPOSE 8000
ENV PYTHONUNBUFFERED=1

CMD ["python", "/app/app/main.py"]
