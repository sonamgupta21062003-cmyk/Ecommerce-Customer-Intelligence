
from pathlib import Path
import pandas as pd
import numpy as np

# Project root and dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "ecommerce_clean_data.csv"

df = pd.read_csv(DATA_PATH)

required = [
    "Quantity",
    "UnitPrice",
    "DiscountPct",
    "SalesAmount",
    "CostPrice",
    "Profit",
]

missing = [col for col in required if col not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# Convert required columns to numeric
for col in required:
    df[col] = pd.to_numeric(df[col], errors="coerce")

valid = df[required].notna().all(axis=1)
audit = df.loc[valid].copy()

# Independently recalculate sales and profit
audit["ExpectedSales"] = (
    audit["Quantity"]
    * audit["UnitPrice"]
    * (1 - audit["DiscountPct"] / 100)
)

audit["ExpectedProfit"] = (
    audit["ExpectedSales"]
    - audit["Quantity"] * audit["CostPrice"]
)

# Compare calculated and stored values
audit["SalesDifference"] = (
    audit["SalesAmount"] - audit["ExpectedSales"]
).abs()

audit["ProfitDifference"] = (
    audit["Profit"] - audit["ExpectedProfit"]
).abs()

tolerance = 0.02

sales_mismatches = audit["SalesDifference"] > tolerance
profit_mismatches = audit["ProfitDifference"] > tolerance

print("\n========== PROFIT CALCULATION AUDIT ==========")
print(f"Dataset rows: {len(df):,}")
print(f"Rows audited: {len(audit):,}")
print(f"Rows skipped due to missing/invalid values: {len(df) - len(audit):,}")

print("\n--- Sales validation ---")
print(f"Sales mismatches: {sales_mismatches.sum():,}")
print(
    "Maximum sales difference:",
    round(audit["SalesDifference"].max(), 4)
)

print("\n--- Profit validation ---")
print(f"Profit mismatches: {profit_mismatches.sum():,}")
print(
    "Maximum profit difference:",
    round(audit["ProfitDifference"].max(), 4)
)

print("\n--- Business checks ---")
print(f"Negative-profit rows: {(audit['Profit'] < 0).sum():,}")
print(f"Zero-profit rows: {(audit['Profit'] == 0).sum():,}")

# Save rows that require investigation
issues = audit.loc[
    sales_mismatches | profit_mismatches
].copy()

output_path = PROJECT_ROOT / "04_Python" / "profit_audit_issues.csv"
issues.to_csv(output_path, index=False)

print(f"\nIssue report saved to: {output_path}")

if sales_mismatches.sum() == 0 and profit_mismatches.sum() == 0:
    print("\nPASS: Stored sales and profit match the formulas.")
else:
    print("\nCHECK REQUIRED: Investigate the mismatched rows.")
