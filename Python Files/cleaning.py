import pandas as pd
import numpy as np
import os

df = pd.read_csv("brfss1_raw.csv")

#recoding data, np.nan = missing/blank value
df["SMOKE100"] = df["SMOKE100"].replace({7: np.nan, 9: np.nan})
print(df["SMOKE100"].value_counts(dropna=False))
print("\n")

#handling multiple features at once, clean disabilities
dis_cols = ["DEAF", "BLIND", "DECIDE", "DIFFWALK", "DIFFDRES", "DIFFALON"]
print(df[dis_cols].value_counts(dropna=False),end="\n\n")

#recode -> replace numerical missing to truely missing
df[dis_cols] = df[dis_cols].replace({7: np.nan, 9: np.nan})

#get percent of missing
print(df[dis_cols].isna().mean(),end="\n\n")

#disability, axis=1 => row, axis=2 => column
df["disabled"] = (df[dis_cols].eq(1).any(axis=1)).astype(int)

#recode to categorical
df["disabled_cat"] = df["disabled"].map({1: "Disabled", 0: "Not Disabled"})

print(df["disabled_cat"])

#binning 
df["_AGEG5YR"] = df["_AGEG5YR"].replace({14: np.nan})
df["_AGEG5YR"].value_counts(dropna=False)
df["age_ymo"] = np.select(
    [
        df["_AGEG5YR"] < 3,
        df["_AGEG5YR"] < 9,
        df["_AGEG5YR"] >= 9
    ],
    ["Young", "Middle", "Old"],
    default="Missing"
)

df["age_ymo"] = df["age_ymo"].replace("Missing", np.nan)
print(df["age_ymo"].value_counts(dropna=False))
df.to_csv("file.csv", index=False)
