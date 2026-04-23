FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY web_app.py .
COPY pytest.ini .
COPY entities/ ./entities/
COPY services/ ./services/
COPY controllers/ ./controllers/
COPY tests/ ./tests/

EXPOSE 5000

CMD ["python", "web_app.py"]
