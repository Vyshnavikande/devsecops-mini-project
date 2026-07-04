FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]