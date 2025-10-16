# 🩺 Virtual Diabetes Clinic — ML Progression Scoring API

This project provides a **machine learning service** that predicts short-term disease progression for diabetes patients.  
It simulates a triage tool used by nurses to identify which patients may need follow-up based on their risk score.

The API is built with **FastAPI** and packaged as a **Docker container**, ready to run locally on any system with **Docker Desktop**.

---

## 🧰 Requirements
Before running, make sure you have:
- **Docker Desktop** installed and running  
  - [Download for Windows/Mac](https://www.docker.com/products/docker-desktop/)
- A working **terminal** (Command Prompt, PowerShell, or Terminal on macOS)
- Internet access to pull the public image from GitHub Container Registry (GHCR)

---

## ⚙️ Available Versions

### 🧩 Version v0.1 — Baseline Model
- **Model:** `StandardScaler + LinearRegression`
- **Purpose:** Baseline prediction of disease progression  
- **Features:** Returns continuous risk score only

**Run commands:**
```bash
docker pull ghcr.io/kasimalsaid/diabetesclinictriage:v0.1
docker run -p 8080:8080 ghcr.io/kasimalsaid/diabetesclinictriage:v0.1
```

**Health check:**
```bash
curl http://localhost:8080/health
```

**Make a prediction:**
```bash
curl -X POST http://localhost:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"age":0.02,"sex":-0.044,"bmi":0.06,"bp":-0.03,"s1":-0.02,"s2":0.03,"s3":-0.02,"s4":0.02,"s5":0.02,"s6":-0.001}'
```

---

### 🚀 Version v0.2 — Improved Model with Risk Calibration
- **Model:** `StandardScaler + Ridge(alpha=1.0)`
- **Improvement:** Adds *calibration of the score* — the API now returns a binary flag (`high_risk`)  
  indicating whether the patient exceeds a defined risk threshold.
- **Output:** Continuous prediction + `high_risk: true/false`

**Run commands:**
```bash
docker pull ghcr.io/kasimalsaid/diabetesclinictriage:v0.2
docker run -p 8080:8080 ghcr.io/kasimalsaid/diabetesclinictriage:v0.2
```

**Health check:**
```bash
curl http://localhost:8080/health
```

**Make a prediction:**
```bash
curl -X POST http://localhost:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"age":0.02,"sex":-0.044,"bmi":0.06,"bp":-0.03,"s1":-0.02,"s2":0.03,"s3":-0.02,"s4":0.02,"s5":0.02,"s6":-0.001}'
```

---

## 🧠 API Overview

### **Endpoints**
| Method | Endpoint | Description |
|--------|-----------|--------------|
| `GET` | `/health` | Returns API status and current model version |
| `POST` | `/predict` | Accepts diabetes dataset features and returns a progression score (and risk flag in v0.2) |

---

## 🔍 Example JSON Input
```json
{
  "age": 0.02,
  "sex": -0.044,
  "bmi": 0.06,
  "bp": -0.03,
  "s1": -0.02,
  "s2": 0.03,
  "s3": -0.02,
  "s4": 0.02,
  "s5": 0.02,
  "s6": -0.001
}
```

---

## 🧾 Notes
- The containers automatically start a FastAPI server on **port 8080**.  
  Make sure this port is available before running.
- Both versions are published to **GitHub Container Registry (GHCR)**:
  - `ghcr.io/kasimalsaid/diabetesclinictriage:v0.1`
  - `ghcr.io/kasimalsaid/diabetesclinictriage:v0.2`
- The models were trained using the open-source **scikit-learn Diabetes dataset** (`load_diabetes`).

---

## 🐳 Useful Docker Commands

**View running containers:**
```bash
docker ps
```

**Stop a running container:**
```bash
docker stop <container_id>
```

**View logs (for debugging):**
```bash
docker logs <container_id>
```

**Remove old containers:**
```bash
docker container prune
```

---

## 👥 Authors
Developed by **Kasim Al-Said - DANIEL HOLM - ISAK HJELM - ELSA STJERNBORG** 

---
