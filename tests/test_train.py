import os
import json
import subprocess
import sys


def test_training_runs_and_artifacts_exist():
    subprocess.check_call([sys.executable, "src/train.py",
                          "--version", "v0.1", "--model", "linear"])
    assert os.path.exists("model/model.pkl")
    assert os.path.exists("artifacts/metrics.json")
    with open("artifacts/metrics.json", "r", encoding="utf-8") as f:
        m = json.load(f)
    assert m["version"] == "v0.1"
    assert "rmse" in m and isinstance(m["rmse"], float)
