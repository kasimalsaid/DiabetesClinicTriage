from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import numpy as np
from src.model_utils import load_model

app = FastAPI(title="Virtual Diabetes Clinic: Progression Scoring API")

try:
    artifacts = load_model()
    model = artifacts["model"]
    scaler = artifacts["scaler"]
    model_version = artifacts.get("version", "unknown")
except Exception as e:
    raise RuntimeError(f"Failed to load model artifact: {e}")


class PatientData(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float


@app.get("/health")
def health():
    return {"status": "ok", "model_version": model_version}


@app.post("/predict")
def predict(payload: PatientData):
    try:
        X = np.array([[
            payload.age, payload.sex, payload.bmi, payload.bp,
            payload.s1, payload.s2, payload.s3, payload.s4, payload.s5, payload.s6
        ]])
        Xs = scaler.transform(X)
        yhat = float(model.predict(Xs)[0])

        response = {"prediction": yhat, "model_version": model_version}

        # Add high-risk flag only for Ridge (v0.2)
        if model_version == "v0.2":
            threshold = 150.0  # Justerbart tröskelvärde
            response["high_risk"] = yhat > threshold

        return response

    except ValidationError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
