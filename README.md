# Virtual Diabetes Clinic — ML Triage (v0.1 & v0.2)

En liten ML-tjänst som förutspår kortsiktig progression i en diabetesklinik.
API körs på **localhost:8080** (Docker Desktop). Byggd med FastAPI + scikit-learn.
CI/CD via GitHub Actions med publicering till GHCR.

## Funktioner
- `GET /health` → `{`"status":"ok","model_version":"vX.Y"`}`
- `POST /predict` → `{`"prediction": <float>, "model_version": "vX.Y"`}`
- Observability: JSON-fel vid ogiltig input (422/400)
- Reproducerbar träning: fixed seeds, versions-pinning, metrics sparas.

## Snabbstart (lokalt)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 1) Träna modellen (default v0.1 = LinearRegression)
python src/train.py --version v0.1 --model linear

# 2) Starta API lokalt (utan Docker)
uvicorn src.predict_service:app --host 0.0.0.0 --port 8080

# 3) Testa
curl http://localhost:8080/health
curl -X POST http://localhost:8080/predict -H "Content-Type: application/json" -d '{"age":0.02,"sex":-0.044,"bmi":0.06,"bp":-0.03,"s1":-0.02,"s2":0.03,"s3":-0.02,"s4":0.02,"s5":0.02,"s6":-0.001}'
```

## Docker (Docker Desktop, port 8080)
```bash
# Träna först så att model/model.pkl finns (välj version)
python src/train.py --version v0.1 --model linear
# eller v0.2 (Ridge):
# python src/train.py --version v0.2 --model ridge

# Bygg image
docker build -t virtual-diabetes-clinic:v0.1 .

# Kör
docker run --rm -p 8080:8080 virtual-diabetes-clinic:v0.1
```

## API-spec
**Request:** (features från `load_diabetes()`)
```json
{
  "age": 0.02, "sex": -0.044, "bmi": 0.06, "bp": -0.03,
  "s1": -0.02, "s2": 0.03, "s3": -0.02, "s4": 0.02, "s5": 0.02, "s6": -0.001
}
```

**Response:**
```json
{"prediction": 123.45, "model_version": "v0.1"}
```

## GitHub Actions
- `ci.yml`: lint, tests, snabbträning, artifacts (`model.pkl`, `metrics.json`)
- `release.yml`: på tag `v*` → tränar, bygger & pushar image till GHCR, smoke-testar, skapar GitHub Release med metrics + CHANGELOG

## Reproducerbarhet
- Seed: 42
- Både data split och modeller använder deterministiska inställningar.
- `metrics.json` sparar RMSE och metadata.

## Versions
- **v0.1**: `StandardScaler` + `LinearRegression`
- **v0.2**: `StandardScaler` + `Ridge(alpha=1.0)`

## Licens
MIT

