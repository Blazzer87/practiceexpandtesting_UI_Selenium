FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN python -m ensurepip && pip install --no-cache-dir -r requirements.txt pytest
COPY . .
CMD ["python", "-m", "pytest", "-q"]