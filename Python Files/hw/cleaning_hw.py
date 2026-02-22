'''
Name: Lucas Hasting
Course: DA 380
Instructor: Dr. Michael Floren
Date: 2/12/2026
Description: Clean the brfss_raw.csv file
'''

#import libraries used
import pandas as pd
import numpy as np

#read in data
df = pd.read_csv("brfss1_raw.csv")

#recode -> replace numerical missing to truely missing (7,9 => blank)
cols_missing = ["EXERANY2", "EDUCA", "SMOKE100", "LANDSEX3", "CELLSEX3", "GENHLTH"]
df[cols_missing] = df[cols_missing].replace({7: np.nan, 9: np.nan})

#recode -> replace numerical missing to truely missing (77, 99 => blank, 88 => 0)
cols_missing = ["SMOKE100", "MENTHLTH", "PHYSHLTH"]
df[cols_missing] = df[cols_missing].replace({77: np.nan, 99: np.nan, 88: 0})

#recode -> replace numerical missing to truely missing (other)
df["INCOME3"] = df["INCOME3"].replace({77: np.nan, 99: np.nan})
df["_AGEG5YR"] = df["_AGEG5YR"].replace({14: np.nan})

#clean disabilities
dis_cols = ["DEAF", "BLIND", "DECIDE", "DIFFWALK", "DIFFDRES", "DIFFALON"]

#recode disabilities -> replace numerical missing to truely missing
df[dis_cols] = df[dis_cols].replace({7: np.nan, 9: np.nan})

#--create new variables as told
df["bmi"] = (df["WTKG3"]/df["HTM4"]**2)*100
df["disabled"] = (df[dis_cols].eq(1).any(axis=1)).astype(int)

#df["sex"] = df["LANDSEX3"].combine_first(df["CELLSEX3"]) => did not actually work, can discuss further if needed (I know the issue)
df["sex"] = np.select(
    [
        df["LANDSEX3"] == 1,
        df["LANDSEX3"] == 2,
        df["CELLSEX3"] == 1,
        df["CELLSEX3"] == 2
    ],
    [1, 0, 1, 0],
    default=-1
)

df["disabled_cat"] = df["disabled"].map({1: "Disabled", 0: "Not Disabled"})
df["sex_cat"] = df["sex"].map({1: "Male", 0: "Female"})
df["phys_healthy_days_30"] = 30 - df["PHYSHLTH"]
df["GENHLTH_pos"] = 6 - df["GENHLTH"]

df["age_ymo"] = np.select(
    [
        df["_AGEG5YR"] <= 3,
        df["_AGEG5YR"] <= 9,
        df["_AGEG5YR"] > 9
    ],
    ["Young", "Middle", "Old"],
    default="Missing"
)

df["bmi_cat"] = np.select(
    [
        df["bmi"] < 18.5, #previous cleaning was 18.5, we were told this should give us that cleaned file
        df["bmi"] < 25,
        df["bmi"] < 30,
        df["bmi"] >= 30,
    ],
    ["Underweight", "Normal", "Overweight", "Obese"],
    default="Missing"
)

df["ment_healthy_days_30"] = 30 - df["MENTHLTH"]

df["obese"] = np.select(
    [
        df["bmi"] > 30,
        df["bmi"] <= 30
    ],
    [1, 0],
    default=-1
)

df["perf_phys_health"] = np.select(
    [
        df["PHYSHLTH"] == 0,
        df["PHYSHLTH"] > 0
    ],
    [1, 0],
    default=-1
)

df["perf_men_health"] = np.select(
    [
        df["MENTHLTH"] == 0,
        df["MENTHLTH"] > 0
    ],
    [1, 0],
    default=-1
)

df["age_bin"] = np.select(
    [
        df["_AGEG5YR"] >= 7,
        df["_AGEG5YR"] < 7
    ],
    [1, 0],
    default=-1
)

df["income_bin"] = np.select(
    [
        df["INCOME3"] >= 8,
        df["INCOME3"] < 8
    ],
    [1, 0],
    default=-1
)

#replace numerical/string encode missing to nan
numerical = ["sex","obese","perf_phys_health","perf_men_health","age_bin","income_bin"]
string = ["age_ymo","bmi_cat"]

df[numerical] = df[numerical].replace({-1: np.nan})
df[string] = df[string].replace({"Missing": np.nan})

#save to the cleaned file
df.to_csv("brfss1_cleaned.csv", index=False)

'''
used to compare to actual cleaned file and see differences (excel/python rounds bmi differently):
df2 = pd.read_csv("brfss1_cleaned(1).csv")
result = df.compare(df2)
result.to_csv("check.csv", index=False)
'''
