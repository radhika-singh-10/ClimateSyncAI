FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl unzip && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn boto3 awscli

COPY . .
COPY ./scripts/fetch_models.sh /usr/local/bin/fetch_models.sh
RUN chmod +x /usr/local/bin/fetch_models.sh

EXPOSE 5000
CMD ["/bin/sh", "-lc", "fetch_models.sh && gunicorn wsgi:application --bind 0.0.0.0:5000 --workers 2 --timeout 120"]
