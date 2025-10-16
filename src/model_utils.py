import json
import joblib
from pathlib import Path
from typing import Any, Dict

MODEL_DIR = Path("model")
ARTIFACTS_DIR = Path("artifacts")
MODEL_DIR.mkdir(parents=True, exist_ok=True)
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


def save_model(bundle: Dict[str, Any], version: str):
    path = MODEL_DIR / "model.pkl"
    joblib.dump({**bundle, "version": version}, path)


def load_model():
    path = MODEL_DIR / "model.pkl"
    return joblib.load(path)


def save_metrics(metrics: Dict[str, Any]):
    path = ARTIFACTS_DIR / "metrics.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
