import pandas as pd
from pathlib import Path

Path("dataset").mkdir(exist_ok=True)

df = pd.read_csv("https://epoch.ai/data/all_ai_models.csv")
df.to_csv("dataset/all_ai_models.csv", index=False)
print(f"Saved {len(df)} models to dataset/all_ai_models.csv")
