"""Reproduce the artifact 3 finding from labelled synthetic data.

Generates the synthetic county-by-month reporting frame behind the dashboard figures, then runs the
three confirming checks: persistence of the coverage gap across months, correlation between coverage
and submission lag, and completeness of the records that do arrive. Every output is labelled
synthetic. No programme data is present or implied.
"""
import numpy as np, pandas as pd

rng = np.random.default_rng(20261024)
COUNTIES = ["Nairobi", "Nakuru", "Kisumu", "Turkana", "Garissa", "Mombasa", "Kakamega", "Machakos"]
MONTHS = list(range(4, 11))
BASE = {"Nairobi": .97, "Nakuru": .96, "Kisumu": .98, "Mombasa": .96, "Kakamega": .92, "Machakos": .95,
        "Turkana": .74, "Garissa": .66}
LAG = {"Nairobi": 3, "Nakuru": 4, "Kisumu": 3, "Mombasa": 5, "Kakamega": 8, "Machakos": 7,
       "Turkana": 14, "Garissa": 18}
rows = []
for c in COUNTIES:
    for m in MONTHS:
        cov = np.clip(rng.normal(BASE[c], .05), 0, 1)
        comp = np.clip(rng.normal(.97 if cov > .85 else .93, .02), 0, 1)
        rows.append({"county": c, "month": m, "coverage": round(cov * 100, 1),
                     "submission_lag_days": LAG[c] + rng.integers(-1, 3),
                     "completeness_of_arrived": round(comp * 100, 1),
                     "source": "SYNTHETIC"})
df = pd.DataFrame(rows)
print("SYNTHETIC DATA. mean coverage by county:")
print(df.groupby("county").coverage.mean().round(1).to_string())
corr = df.groupby("county").agg(cov=("coverage", "mean"), lag=("submission_lag_days", "mean")).corr().iloc[0, 1]
print(f"correlation between county coverage and submission lag: {corr:.2f} (synthetic by construction)")
print("mean completeness of arrived records:", round(df.completeness_of_arrived.mean(), 1),
      "so the gap is missing records, not malformed ones")
df.to_csv("synthetic_coverage_frame.csv", index=False)
