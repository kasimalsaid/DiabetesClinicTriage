import joblib
import json
from pathlib import Path


def save_model(artifacts, version: str):
    Path("model").mkdir(exist_ok=True)
    path = Path(f"model/model_{version}.pkl")
    joblib.dump(artifacts, path)


def load_model(version: str = None):
    model_dir = Path("model")
    if version:
        path = model_dir / f"model_{version}.pkl"
    else:
        # Ladda senaste modell
        models = sorted(model_dir.glob("model_*.pkl"))
        if not models:
            raise FileNotFoundError("No model artifacts found.")
        path = models[-1]
    return joblib.load(path)


def save_metrics(metrics: dict):
    Path("artifacts").mkdir(exist_ok=True)
    with open("artifacts/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
