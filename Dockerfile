FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN python -m ensurepip && pip install --no-cache-dir -r requirements.txt
COPY . .

