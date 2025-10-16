# Changelog

## v0.2
- Modell: `StandardScaler + Ridge(alpha=1.0)`
- Förbättringar: bättre bias–variance tradeoff än OLS.
- Resultat: se `artifacts/metrics.json` för RMSE.
- API: oförändrat svar men `"model_version" = "v0.2"`.

## v0.1
- Baslinje: `StandardScaler + LinearRegression`
- Artefakter: `model/model_v0.1.pkl`, `artifacts/metrics.json`
- API: `/health`, `/predict`
- Docker: exponerar port 8080, självbärande image.
