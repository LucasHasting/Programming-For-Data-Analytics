'''
Name: Lucas Hasting
Course: DA 380
Instructor: Dr. Michael Floren
Date: 2/24/2026
Description: Get inferential stats from brfss1_cleaned.cvs
'''

#import needed libraries
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

#load the data
df = pd.read_csv("brfss1_cleaned.csv")

#is general health different between people who exercise vs. not? - T-TEST
print("GENHLTH vs. EXERANY2:",end="\n\n")
gen_hlth_exer = df.loc[df["EXERANY2"] == 1, "GENHLTH"].dropna()
gen_hlth_not_exer = df.loc[df["EXERANY2"] == 2, "GENHLTH"].dropna()

print(stats.ttest_ind(gen_hlth_not_exer, gen_hlth_exer, equal_var=False),end="\n\n")
print("Exercise:\n",gen_hlth_exer.agg(["mean", "std"]),end="\n\n",sep="")
print("No Exercise:\n",gen_hlth_not_exer.agg(["mean", "std"]),end="\n\n",sep="")

#general health across income groups - are they different? - ANOVA
print("INCOME3 vs. GENHLTH:",end="\n\n")
df["INCOME3_no_na"] = df["INCOME3"].dropna()
df["GENHLTH_no_na"] = df["GENHLTH"].dropna()
model_genhlth = smf.ols("GENHLTH_no_na ~ C(INCOME3_no_na)", data=df).fit()
print(sm.stats.anova_lm(model_genhlth))
print(df.groupby("INCOME3_no_na")["GENHLTH_no_na"].agg(["mean", "std"]),end="\n\n")

#association between exercise participation and median annual household income? - Ch^2

print("INCOME3 vs. GENHLTH:",end="\n\n")
df["EXERANY2_no_na"] = df["EXERANY2"].dropna()
df["income_bin_no_na"] = df["income_bin"].dropna()
print(df.groupby("EXERANY2_no_na")["income_bin_no_na"].value_counts())
print(stats.chi2_contingency(pd.crosstab(df["income_bin_no_na"], df["EXERANY2_no_na"])),end="\n\n")

#BMI linearily correlated with disabled and exercise participation? - OLS Regression

print("BMI vs. EXERANY2 and disabled:",end="\n\n")
df["BMI_no_na"] = df["bmi"].dropna()
df["disabled_no_na"] = df["disabled"].dropna()
model_bmi = smf.ols("BMI_no_na ~ C(EXERANY2_no_na) + C(disabled_no_na)", data=df).fit()
print(sm.stats.anova_lm(model_bmi))
print(model_bmi.summary())
