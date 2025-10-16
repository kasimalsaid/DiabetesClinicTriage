import argparse
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error

from model_utils import save_model, save_metrics

SEED = 42

def train(version: str, model_name: str):
    data = load_diabetes(as_frame=True)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED, shuffle=True
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    if model_name.lower() == "ridge":
        model = Ridge(alpha=1.0, random_state=SEED)
    elif model_name.lower() == "linear":
        model = LinearRegression()
    else:
        raise ValueError("Unknown model. Use 'linear' or 'ridge'.")

    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)
    rmse = float(np.sqrt(mean_squared_error(y_test, preds)))

    save_model({"model": model, "scaler": scaler}, version)
    metrics = {
        "version": version,
        "model": model.__class__.__name__,
        "rmse": rmse,
        "seed": SEED,
        "n_train": int(X_train.shape[0]),
        "n_test": int(X_test.shape[0]),
    }
    save_metrics(metrics)
    print(f"✅ Training complete | version={version} model={model_name} RMSE={rmse:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v0.1")
    parser.add_argument("--model", default="linear", choices=["linear", "ridge"])
    args = parser.parse_args()
    train(args.version, args.model)
