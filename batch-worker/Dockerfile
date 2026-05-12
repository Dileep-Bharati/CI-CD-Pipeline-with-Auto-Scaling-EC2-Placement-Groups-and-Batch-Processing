FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY batch_worker.py .

ENV AWS_REGION=us-east-1
ENV SQS_QUEUE_URL=""
ENV S3_OUTPUT_BUCKET=""

CMD ["python", "batch_worker.py"]
