# 1. Basbild
FROM python:3.11-slim

# 2. Sätt arbetskatalog
WORKDIR /app

# 3. Kopiera requirements och installera beroenden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopiera hela koden
COPY . .

# 5. Kör träning innan API startar
#    (du kan välja v0.1 eller v0.2 beroende på version)
RUN python src/train.py --version v0.1 --model linear

# 6. Exponera port för FastAPI
EXPOSE 8080

# 7. Startkommando
CMD ["uvicorn", "src.predict_service:app", "--host", "0.0.0.0", "--port", "8080"]
