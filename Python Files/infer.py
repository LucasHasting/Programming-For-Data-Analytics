import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

#load the data
df = pd.read_csv("brfss1_cleaned.csv")

print(stats.norm.cdf(1.96))  #left of the curve
print(stats.norm.ppf(0.975)) #inv-norm

#is mean BMI different between adults with/without disability

bmi_dis = df.loc[df["disabled"] == 1, "bmi"].dropna()
bmi_not_dis = df.loc[df["disabled"] == 0, "bmi"].dropna()

#.agg(["stat",...])

#--T-TEST

print()
print(stats.ttest_ind(bmi_dis, bmi_not_dis, equal_var=False),end="\n\n")
print("BMI-dis => mean, std: ", bmi_dis.mean(), bmi_dis.std())
print("BMI-not-dis => mean, std: ", bmi_not_dis.mean(), bmi_not_dis.std())

#sex?
bmi_male = df.loc[df["sex_cat"] == "Male", "bmi"].dropna()
bmi_female = df.loc[df["sex_cat"] == "Female", "bmi"].dropna()

print()
print(stats.ttest_ind(bmi_male, bmi_female, equal_var=False),end="\n\n")
print("BMI-male => mean, std: ", bmi_male.mean(), bmi_male.std())
print("BMI-female => mean, std: ", bmi_female.mean(), bmi_female.std())

#--ANOVA

#across age groups

model = smf.ols("bmi ~ C(age_ymo)", data=df).fit()
print(sm.stats.anova_lm(model))
print(df.groupby("age_ymo")["bmi"].agg(["mean", "std"]),end="\n\n")

#--Chi^2

#disability status with smpoking history

table = pd.crosstab(df["disabled"], df["SMOKE100"])
print(stats.chi2_contingency(table),end="\n\n")

#--Regression

#BMI with physical/mental health

model_reg = smf.ols("bmi ~ phys_healthy_days_30 + ment_healthy_days_30", data=df).fit()
print(model_reg.summary())
