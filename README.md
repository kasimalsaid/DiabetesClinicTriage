# 🩺 Virtual Diabetes Clinic — ML Progression Scoring API

This project provides a **machine learning service** that predicts short-term disease progression for diabetes patients.  
It simulates a triage tool used by nurses to identify which patients may need follow-up based on their risk score.

The API is built with **FastAPI** and packaged as a **Docker container**, ready to run locally on any system with **Docker Desktop**.

---

## 🧰 Prerequisites
Make sure you have:
- **Docker Desktop** installed and running  
  - [Download for Windows/Mac](https://www.docker.com/products/docker-desktop/)
- **Internet connection**
- A **terminal** (PowerShell on Windows or Terminal on macOS/Linux)

---

## 🩺 Test the ML API — Diabetes Clinic Triage

### 🧩 1️⃣ Pull the images
Version 0.1
```bash
docker pull ghcr.io/kasimalsaid/diabetesclinictriage:v0.1
```
Version 0.2
```bash
docker pull ghcr.io/kasimalsaid/diabetesclinictriage:v0.2
```
---

### 🚀 2️⃣ Run the container
Example for **v0.1 Ridge Regression**:
```bash
docker run -p 8080:8080 ghcr.io/kasimalsaid/diabetesclinictriage:v0.1
```

> 💡 Replace `v0.1` with `v0.2` to run the baseline Ridge Regression model.

---

### ❤️ 3️⃣ Health check

#### 🪟 **Windows PowerShell / VS Code**
```powershell
curl http://localhost:8080/health
```

#### 🍎 **macOS / Linux Terminal**
```bash
curl http://localhost:8080/health
```

Expected output:
```json
{"status":"ok","model_version":"v0.2"}
```

---

### 🧠 4️⃣ Make a prediction

#### 🪟 **Windows PowerShell / VS Code**
```powershell
$headers = @{
  "Content-Type" = "application/json"
}

$body = '{
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
}'

$response = Invoke-WebRequest -Uri "http://localhost:8080/predict" -Method POST -Headers $headers -Body $body
$response.Content
```

---

#### 🍎 **macOS / Linux Terminal**
```bash
curl -X POST http://localhost:8080/predict      -H "Content-Type: application/json"      -d '{"age":0.02,"sex":-0.044,"bmi":0.06,"bp":-0.03,"s1":-0.02,"s2":0.03,"s3":-0.02,"s4":0.02,"s5":0.02,"s6":-0.001}'
```

---

### 🔁 Versions
| Version | Model Type | Description |
|----------|-------------|-------------|
| v0.1 | Linear Regression | Baseline model using StandardScaler + LinearRegression |
| v0.2 | Ridge Regression | Improved model with Ridge regularization and risk calibration |

---

## 🧠 API Overview

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

## 👥 Author
Developed by **Kasim Al-Saaid - Daniel Holm - Isak Hjelm - Elsa Stjernborg** 

---
